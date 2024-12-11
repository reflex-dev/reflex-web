import json

from .document import Document
from .logger import logger


class Documents(object):
    RESOURCE_PATH = 'documents'

    def __init__(self, api_call, collection_name):
        self.api_call = api_call
        self.collection_name = collection_name
        self.documents = {}

    def __getitem__(self, document_id):
        if document_id not in self.documents:
            self.documents[document_id] = Document(self.api_call, self.collection_name, document_id)

        return self.documents[document_id]

    def _endpoint_path(self, action=None):
        from .collections import Collections

        action = action or ''
        return u"{0}/{1}/{2}/{3}".format(Collections.RESOURCE_PATH, self.collection_name, Documents.RESOURCE_PATH,
                                         action)

    def create(self, document, params=None):
        params = params or {}
        params['action'] = 'create'
        return self.api_call.post(self._endpoint_path(), document, params)

    def create_many(self, documents, params=None):
        logger.warning('`create_many` is deprecated: please use `import_`.')
        return self.import_(documents, params)

    def upsert(self, document, params=None):
        params = params or {}
        params['action'] = 'upsert'
        return self.api_call.post(self._endpoint_path(), document, params)

    def update(self, document, params=None):
        params = params or {}
        params['action'] = 'update'
        return self.api_call.post(self._endpoint_path(), document, params)

    def import_jsonl(self, documents_jsonl):
        logger.warning('`import_jsonl` is deprecated: please use `import_`.')
        return self.import_(documents_jsonl)

    # `documents` can be either a list of document objects (or)
    #  JSONL-formatted string containing multiple documents
    def import_(self, documents, params=None):
        if isinstance(documents, list):
            document_strs = []
            for document in documents:
                document_strs.append(json.dumps(document))

            docs_import = '\n'.join(document_strs)
            api_response = self.api_call.post(self._endpoint_path('import'), docs_import, params, as_json=False)
            res_obj_strs = api_response.split('\n')

            response_objs = []
            for res_obj_str in res_obj_strs:
                response_objs.append(json.dumps(res_obj_str))

            return response_objs
        else:
            api_response = self.api_call.post(self._endpoint_path('import'), documents, params, as_json=False)
            return api_response

    def export(self, params=None):
        api_response = self.api_call.get(self._endpoint_path('export'), params, as_json=False)
        return api_response

    def search(self, search_parameters):
        return self.api_call.get(self._endpoint_path('search'), search_parameters)

    def delete(self, params=None):
      return self.api_call.delete(self._endpoint_path(), params)
