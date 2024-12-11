
from ctypes import Union


class Operations(object):
    RESOURCE_PATH = '/operations'
    HEALTH_PATH = '/health'

    def __init__(self, api_call):
        self.api_call = api_call

    @staticmethod
    def _endpoint_path(operation_name):
        return u"{0}/{1}".format(Operations.RESOURCE_PATH, operation_name)


    def perform(self, operation_name, query_params=None):
        query_params = query_params or {}
        return self.api_call.post(self._endpoint_path(operation_name), {}, query_params)
    
    def is_healthy(self)-> bool:
        call_resp = self.api_call.get(Operations.HEALTH_PATH)
        return call_resp.get("ok", False) if isinstance(call_resp, dict) else False
