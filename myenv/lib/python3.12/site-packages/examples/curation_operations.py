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

# Create a collection

create_response = client.collections.create({
  "name": "books",
  "fields": [
    {"name": "title", "type": "string" },
    {"name": "authors", "type": "string[]", "facet": True },
    {"name": "publication_year", "type": "int32", "facet": True },
    {"name": "ratings_count", "type": "int32" },
    {"name": "average_rating", "type": "float" },
    {"name": "image_url", "type": "string" }
  ],
  "default_sorting_field": "ratings_count"
})

print(create_response)

# Create or update an override

create_override_response = client.collections["books"].overrides.upsert('hermione-exact', {
  "rule": {
    "query": "hermione",
    "match": "exact"
  },
  "includes": [
    {"id": "1", "position": 1},
  ]
})

print(create_override_response)

# List all overrides

print(client.collections["books"].overrides.retrieve())

# Retrieve the configuration of a specific override

print(client.collections["books"].overrides["hermione-exact"].retrieve())

# Add a book

hunger_games_book = {
  'id': '1', 'original_publication_year': 2008, 'authors': ['JK Rowling'], 'average_rating': 4.34,
  'publication_year': 2008,
  'title': 'Harry Potter and the Goblet of Fire',
  'image_url': 'https://images.gr-assets.com/books/1447303603m/2767052.jpg',
  'ratings_count': 4780653
}

client.collections['books'].documents.create(hunger_games_book)

# Search for a book

print(client.collections['books'].documents.search({
    'q': 'hermione',
    'query_by': 'title',
    'sort_by': 'ratings_count:desc'
}))

# Delete an override

print(client.collections['books'].overrides["hermione-exact"].delete())
