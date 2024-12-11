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
  "name": "books_january",
  "fields": [
    {"name": "title", "type": "string" },
    {"name": "authors", "type": "string[]", "facet": True  },
    {"name": "publication_year", "type": "int32", "facet": True  },
    {"name": "ratings_count", "type": "int32" },
    {"name": "average_rating", "type": "float" },
    {"name": "image_url", "type": "string" }
  ],
  "default_sorting_field": "ratings_count"
})

print(create_response)

# Create or update an existing alias

create_alias_response = client.aliases.upsert('books_link', {
    "collection_name": "books_january"
})

print(create_alias_response)

# Add a book using the alias name `books`

hunger_games_book = {
  'id': '1', 'original_publication_year': 2008, 'authors': ['Suzanne Collins'], 'average_rating': 4.34,
  'publication_year': 2008, 'title': 'The Hunger Games',
  'image_url': 'https://images.gr-assets.com/books/1447303603m/2767052.jpg',
  'ratings_count': 4780653
}

client.collections['books_link'].documents.create(hunger_games_book)

# Search using the alias

print(client.collections['books_link'].documents.search({
    'q': 'hunger',
    'query_by': 'title',
    'sort_by': 'ratings_count:desc'
}))

# List all aliases

print(client.aliases.retrieve())

# Retrieve the configuration of a specific alias

print(client.aliases['books_link'].retrieve())

# Delete an alias

print(client.aliases['books_link'].delete())
