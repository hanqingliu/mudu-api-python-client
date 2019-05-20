import collections
import hashlib
import time
import urllib3
import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

def gen_signed_params(ak, sk, kwargs):
    args = {}
    for k,v in kwargs.items():
        args[k] = str(v)
    args['access_key'] = ak
    args['secret_key'] = sk
    args['timestamp'] = str(int(time.time()))
    od = collections.OrderedDict(sorted(args.items()))
    sign = hashlib.sha1(json.dumps(od, separators=(',',':'))).hexdigest()

    ret_args = {
        'timestamp': args['timestamp'],
        'access_key': ak,
        'sign': sign
    }
    return ret_args


class MuduApiClient(object):

    BASE_URL = 'https://hwyouke.mudu.tv/console/index.php'

    def __init__(self, access_key, secret_key, url=None):
        self.access_key = access_key
        self.secret_key = secret_key
        self.BASE_URL = url if url else self.BASE_URL
        self.connection_pool = self._make_connection_pool()

    def _make_connection_pool(self):
        return urllib3.PoolManager()

    def _compose_url(self, params):
        return self.BASE_URL + '?' + urlencode(params)

    def _handle_response(self, response):
        try:
            return json.loads(response.data)
        except Exception:
            return {'code': 500, 'msg':'Invalid response'}

    def _request(self, method, resource, action, params=None):
        signed_params = gen_signed_params(self.access_key, self.secret_key, params)
        signed_params['c'] = resource
        signed_params['a'] = action
        url = self._compose_url(signed_params)
        r = self.connection_pool.request_encode_body(
            method.upper(),
            url,
            fields=params,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'accept': 'application/json'
            },
            encode_multipart=False)
        return self._handle_response(r)

    def call(self, method, resource, action, **params):
        return self._request(method, resource, action, params=params)
        
