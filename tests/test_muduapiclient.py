import ddt
import mock
from unittest import TestCase
from muduapiclient.client import MuduApiClient, gen_signed_params
import time

@ddt.ddt
class MuduApiClientTests(TestCase):

    @ddt.unpack
    @ddt.data(
        ('ACCESS_KEY', 'SECRET_KEY', {'page':1, 'live_status':2}),
    )
    def test_gen_signed_params(self, ak, sk, kwargs):
        original_time = time.time
        time.time = mock.Mock(return_value='1234567890')
        signed_params = gen_signed_params(ak, sk, kwargs)
        time.time = original_time
        self.assertIn('sign', signed_params)
        self.assertEqual(signed_params['sign'], 'af7470c6f59d051c633401d1fd0b86fd1aa05352')
        self.assertNotIn('secret_key', signed_params)


    @ddt.unpack
    @ddt.data(
        ('ACCESS_KEY', 'SECRET_KEY', {'page':1, 'live_status':2}),
        ('507cfcdfe351e13e6f1c8ba87b80969f', 'SECRET_KEY', {'page':1, 'live_status':4}),
    )
    def test_call_live(self, ak, sk, kwargs):
        api = MuduApiClient(ak, sk)
        response = api.call('POST', 'live', 'List', **kwargs)
        self.assertIn('code', response)
