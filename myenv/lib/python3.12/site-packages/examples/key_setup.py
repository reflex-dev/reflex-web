import typesense,json

client = typesense.Client({
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'api_key': 'abcd',
  'connection_timeout_seconds': 2
})

create_response = client.collections.create({
    "name": "collA",
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "publication_year", "type": "int32", "facet": True},
    ]
})

print(create_response)

create_response = client.collections.create({
    "name": "collB",
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "publication_year", "type": "int32", "facet": True},
    ]
})

print(create_response)

# Add a document to both collections
hunger_games_bookA = {
    'id': '1',
    'title': 'The Hunger Games',
    'publication_year': 2008,
}

hunger_games_bookB = {
    'id': '1',
    'title': 'The Hunger Games',
    'publication_year': 2010,
}

client.collections['collA'].documents.create(hunger_games_bookA)
client.collections['collB'].documents.create(hunger_games_bookB)

# Create 2 parent keys for each collection

keyA = client.keys.create({"description": "Search-only CollA key.", "actions": ["documents:search"], "collections": ["collA"], "value": "keyprefixa"})
print(keyA)

keyB = client.keys.create({"description": "Search-only CollB key.", "actions": ["documents:search"], "collections": ["collB"], "value": "keyprefixb"})
print(keyB)

# Create 2 scoped API keys

scoped_search_keyA = client.keys.generate_scoped_search_key(keyA['value'], {"filter_by": "publication_year: 2008"})
print(scoped_search_keyA)

scoped_search_keyB = client.keys.generate_scoped_search_key(keyB['value'], {"filter_by": "publication_year: 2010"})
print(scoped_search_keyB)


