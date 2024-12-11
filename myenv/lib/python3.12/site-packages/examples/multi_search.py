import typesense
import json

# Make multi search

search_client = typesense.Client({
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'api_key': 'keyprefixa',
  'connection_timeout_seconds': 2
})

multi_search_res = search_client.multi_search.perform({'searches': [
    {
        'collection': "collA",
        'q': 'hunger',
        'query_by': 'title',
        "x-typesense-api-key": 'ZDlTSVpteUdRWmdabGFFc3hFdG91NUxQdUttLzkvTnIrWklFd2o3b1EvMD1rZXlweyJmaWx0ZXJfYnkiOiAicHVibGljYXRpb25feWVhcjogMjAwOCJ9',
    },
    {
        'collection': "collB",
        'q': 'hunger',
        'query_by': 'title',
        "x-typesense-api-key": 'MGlzRDhuMHpGR2NwK3VTNnd3cHlQUHN2TEVlaWNuZ2F0dGExb2c0VXlEOD1rZXlweyJmaWx0ZXJfYnkiOiAicHVibGljYXRpb25feWVhcjogMjAxMCJ9',
    }
]},{})

print(json.dumps(multi_search_res))