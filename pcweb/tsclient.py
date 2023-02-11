import typesense

client = typesense.Client({
  'api_key': 'your_api_key',
  'nodes': [{
    'host': 'xxx.a1.typesense.net',
    'port': '443',
    'protocol': 'https'
  }],
  'connection_timeout_seconds': 2
})