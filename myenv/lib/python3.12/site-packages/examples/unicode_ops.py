import json
import os
import sys
import typesense


curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.abspath(os.path.join(curr_dir, os.pardir)))


client = typesense.Client({
    'api_key': 'abcd',
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
})

# Drop pre-existing collection if any
try:
    client.collections['titles'].delete()
except Exception as e:
    pass

# Create a collection

create_response = client.collections.create({
    "name": "titles",
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "points", "type": "int32" }
    ],
    "default_sorting_field": "points"
})

print(create_response)

with open('/tmp/unicode.jsonl') as jsonl_file:
    client.collections['titles'].documents.import_(jsonl_file.read(), {'action': 'create'})
