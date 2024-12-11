class Alias(object):
    def __init__(self, api_call, name):
        self.api_call = api_call
        self.name = name

    def _endpoint_path(self):
        from .aliases import Aliases
        return u"{0}/{1}".format(Aliases.RESOURCE_PATH, self.name)

    def retrieve(self):
        return self.api_call.get(self._endpoint_path())

    def delete(self):
        return self.api_call.delete(self._endpoint_path())
