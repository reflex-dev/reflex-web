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
    client.collections['books'].delete()
except Exception as e:
    pass

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

# Create or update a synonym

create_synonym_response = client.collections["books"].synonyms.upsert('hp-philosopher-sorcerer', {
  "synonyms": ["philosophers", "sorcerers"]
})

print(create_synonym_response)

# List all synonyms

print(client.collections["books"].synonyms.retrieve())

# Retrieve the configuration of a specific synonym

print(client.collections["books"].synonyms["hp-philosopher-sorcerer"].retrieve())

# Add a book

hp_book = {
  'id': '1', 'original_publication_year': 2001, 'authors': ['JK Rowling'], 'average_rating': 4.34,
  'publication_year': 2001,
  'title': 'Harry Potter and the Philosopher\'s Stone',
  'image_url': 'https://images.gr-assets.com/books/1447303603m/2767052.jpg',
  'ratings_count': 4780653
}

client.collections['books'].documents.create(hp_book)

# Search for a book

print(client.collections['books'].documents.search({
    'q': 'sorcerers',
    'query_by': 'title',
    'sort_by': 'ratings_count:desc'
}))

# Update synonym: convert to 1-way synonym
update_synonym_response = client.collections["books"].synonyms.upsert('hp-philosopher-sorcerer', {
  "root": "philosophers", "synonyms": ["sorcerers"]
})

print(update_synonym_response)

print(client.collections["books"].synonyms.retrieve())

# Search again, but we won't find it now since we have updated it to 1-way

print(client.collections['books'].documents.search({
    'q': 'sorcerers',
    'query_by': 'title',
    'sort_by': 'ratings_count:desc'
}))

# Delete an synonym

print(client.collections['books'].synonyms["hp-philosopher-sorcerer"].delete())
