
class MultiSearch(object):
    RESOURCE_PATH = '/multi_search'

    def __init__(self, api_call):
        self.api_call = api_call

    def perform(self, search_queries, common_params):
        return self.api_call.post(MultiSearch.RESOURCE_PATH, search_queries, common_params)
