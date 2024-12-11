import os
import sys
import json
import typesense


curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.abspath(os.path.join(curr_dir, os.pardir)))


client = typesense.Client({
    'api_key': 'abcd',
    'nodes': [
        {
            'host': 'localhost',
            'port': '8108',
            'protocol': 'http'
        },
        {
            'host': 'localhost',
            'port': '7108',
            'protocol': 'http'
        },
        {
            'host': 'localhost',
            'port': '6108',
            'protocol': 'http'
        }
    ],
    'connection_timeout_seconds': 10
})

# Drop pre-existing collection if any
try:
    client.collections['books'].delete()
except Exception as e:
    pass

schema = {
    "name": "books",
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "authors", "type": "string[]", "facet": True },
        {"name": "publication_year", "type": "int32", "facet": True },
        {"name": "ratings_count", "type": "int32"},
        {"name": "average_rating", "type": "float"},
        {"name": "image_url", "type": "string"}
    ],
    "default_sorting_field": "ratings_count"
}

create_response = client.collections.create(schema)

print(create_response)

# Let's use bulk import
book_documents = []
with open('/tmp/books.jsonl') as infile:
    for json_line in infile:
        book_documents.append(json.loads(json_line))

print('')
print(client.collections['books'].documents.create_many(book_documents))

i = 0
while i < 10000:
    res = client.collections['books'].documents.search({
        'q': 'the',
        'query_by': 'title',
        'sort_by': 'ratings_count:desc'
    })
    print(res['found'])
