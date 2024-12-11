import typesense
import json

client = typesense.Client({
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'api_key': 'abcd',
  'connection_timeout_seconds': 2
})

client.collections.create({
  'name': 'products',
  'fields': [
    {'name': 'name', 'type': 'string'},
    {'name': 'description', 'type': 'string'},
    {'name': 'price', 'type': 'float'}
  ]
})

client.collections['products'].documents.create({
  'name': 'Nike Running Shoe',
  'description': 'Running shoe by Nike.',
  'price': 50
})

client.collections['products'].documents.search({
  'q': 'running shoes',
  'query_by': 'title,description',
  'filter_by': 'price:<100',
  'sort_by': 'popularity_score:desc',
})
