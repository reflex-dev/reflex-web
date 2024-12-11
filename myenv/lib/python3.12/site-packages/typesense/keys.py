import base64
import hashlib
import hmac
import json

from .key import Key


class Keys(object):
    RESOURCE_PATH = '/keys'

    def __init__(self, api_call):
        self.api_call = api_call
        self.keys = {}

    def __getitem__(self, key_id):
        if key_id not in self.keys:
            self.keys[key_id] = Key(self.api_call, key_id)

        return self.keys.get(key_id)

    def create(self, schema):
        return self.api_call.post(Keys.RESOURCE_PATH, schema)

    def generate_scoped_search_key(self, search_key, parameters):
        # Note: only a key generated with the `documents:search` action will be accepted by the server
        params_str = json.dumps(parameters)
        digest = base64.b64encode(
            hmac.new(search_key.encode('utf-8'), params_str.encode('utf-8'), digestmod=hashlib.sha256).digest()
        )
        key_prefix = search_key[0:4]
        raw_scoped_key = '{}{}{}'.format(digest.decode('utf-8'), key_prefix, params_str)
        return base64.b64encode(raw_scoped_key.encode('utf-8'))

    def retrieve(self):
        return self.api_call.get('{0}'.format(Keys.RESOURCE_PATH))
