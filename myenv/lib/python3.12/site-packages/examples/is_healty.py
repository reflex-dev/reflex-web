import typesense
from time import time

client = typesense.Client({
  'api_key': 'abcd',
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 2
})


# Create a collection

while not client.operations.is_healthy():
  print("cluster is unhealthy, retrying...")
  time.sleep(1)
print("cluster is healthy")



