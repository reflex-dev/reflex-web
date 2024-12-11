from .collection import Collection


class Collections(object):
    RESOURCE_PATH = '/collections'

    def __init__(self, api_call):
        self.api_call = api_call
        self.collections = {}

    def __getitem__(self, collection_name):
        if collection_name not in self.collections:
            self.collections[collection_name] = Collection(self.api_call, collection_name)

        return self.collections.get(collection_name)

    def create(self, schema):
        return self.api_call.post(Collections.RESOURCE_PATH, schema)

    def retrieve(self):
        return self.api_call.get('{0}'.format(Collections.RESOURCE_PATH))
