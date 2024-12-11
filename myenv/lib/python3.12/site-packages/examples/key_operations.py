import typesense

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
    client.collections['key_collection'].delete()
except Exception as e:
    pass

# Create a collection with admin key
create_response = client.collections.create({
    "name": "key_collection",
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "ratings_count", "type": "int32"},
    ],
    "default_sorting_field": "ratings_count"
})

# Add a document
document = {
  'id': '1',
  'title': 'The Hunger Games',
  'ratings_count': 200
}
client.collections['key_collection'].documents.create(document)

# Create a new key
key = client.keys.create({"description": "Search-only key.", "actions": ["documents:search"], "collections": ["key_collection"]})
print(key)

# Try to fetch it back
print(client.keys[key['id']].retrieve())

# Create a search client using this key
search_client = typesense.Client({
    'api_key': key['value'],
    'nodes': [{
      'host': 'localhost',
      'port': '8108',
      'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
})

# Try to create a collection from a new client using this search key (should fail)
try:
  create_response = search_client.collections.create({
      "name": "key_collection2",
      "fields": [
          {"name": "title", "type": "string"},
          {"name": "ratings_count", "type": "int32"},
      ],
      "default_sorting_field": "ratings_count"
  })

  print(create_response)
except Exception as e:
  print(e)

# Generate scoped search key
scoped_search_key = client.keys.generate_scoped_search_key(key['value'], {"filter_by": "ratings_count:<100"})
print(scoped_search_key)

# Search collection
print(search_client.collections['key_collection'].documents.search({
    'q': 'hunger',
    'query_by': 'title',
    'sort_by': 'ratings_count:desc'
}))

# Create a scoped client and search with that
scoped_search_client = typesense.Client({
    'api_key': scoped_search_key,
    'nodes': [{
      'host': 'localhost',
      'port': '8108',
      'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
})

# Search again, will be restricted to `ratings_count:<100` so no record will be returned
print(scoped_search_client.collections['key_collection'].documents.search({
    'q': 'hunger',
    'query_by': 'title',
    'filter_by': 'ratings_count:>100',  # trying to override the embedded filter
    'sort_by': 'ratings_count:desc'
}))

# Delete the key
print(client.keys[key['id']].delete())

# List all keys
print(client.keys.retrieve())
