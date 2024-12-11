from .overrides import Overrides
from .synonyms import Synonyms
from .documents import Documents


class Collection(object):
    def __init__(self, api_call, name):
        self.name = name
        self.api_call = api_call
        self.documents = Documents(api_call, name)
        self.overrides = Overrides(api_call, name)
        self.synonyms = Synonyms(api_call, name)

    def _endpoint_path(self):
        from .collections import Collections
        return u"{0}/{1}".format(Collections.RESOURCE_PATH, self.name)

    def retrieve(self):
        return self.api_call.get(self._endpoint_path())

    def update(self, schema_change):
        return self.api_call.patch(self._endpoint_path(), schema_change)

    def delete(self):
        return self.api_call.delete(self._endpoint_path())
