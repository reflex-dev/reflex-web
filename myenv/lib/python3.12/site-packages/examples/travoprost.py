import typesense,json

t_client = typesense.Client({
  'nodes': [{
    'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
    'port': '8108',      # For Typesense Cloud use 443
    'protocol': 'http'   # For Typesense Cloud use https
  }],
  'api_key': 'abcd',
  'connection_timeout_seconds': 2
})


pharma_schema = {
  'name': 'idi',
  'fields': [
    {"name": ".*", "type": "auto" },
    {'name': 'title', 'type': 'string','facet':True },
    {'name': 'content_type', 'type': 'string','facet':True }
  ]
}

try:
    t_client.collections['idi'].delete()
except Exception as e:
    pass

print(t_client.collections.create(pharma_schema))

docs = [
    {"_id": "579854e1fa02c04d3c8757db", "body": "puppy runs crazily. adorable", "content_type": "pharma", "id": "0",
     "title": "Amphetamine"},
    {"_id": "579856fefa02c04d3c8757e6", "body": "monkey barfs occasionally. stupid", "content_type": "pharma",
     "id": "1", "title": "Prazosin"},
    {"_id": "57985715fa02c04d3c8757e7", "body": "monkey barfs occasionally. stupid", "content_type": "pharma",
     "id": "2", "title": "Terazosin"},
    {"_id": "57985c24fa02c04d3c875821", "body": "monkey barfs occasionally. stupid", "content_type": "pharma",
     "id": "3", "title": "Timolol"},
    {"_id": "57985c43fa02c04d3c875825", "body": "puppy runs crazily. adorable", "content_type": "pharma", "id": "4",
     "title": "Betaxolol"},
    {"_id": "57985d5ffa02c04d3c875841", "body": "puppy runs crazily. adorable", "content_type": "pharma", "id": "5",
     "title": "Travoprost"},
    {"_id": "57556293fa02c05bad8805ea", "body": "rabbit jumps foolishly. dirty", "content_type": "pharma", "id": "6",
     "title": "Aminoacridine "},
    {"_id": "57556293fa02c05bad8805eb", "body": "car hits dutifully. clueless", "content_type": "pharma", "id": "7",
     "title": "Antitrematodal"},
    {"_id": "57556293fa02c05bad8805ec", "body": "rabbit jumps foolishly. dirty", "content_type": "pharma", "id": "8",
     "title": "Tubulin Binder"},
    {"_id": "57556293fa02c05bad8805ed", "body": "girl drives merrily. odd", "content_type": "pharma", "id": "9",
     "title": "Benzimidazole "},
]

for doc in docs:
    print(t_client.collections['idi'].documents.create(doc))

print(t_client.collections['idi'].documents.search({
  'q'         : 'Travoprost',
  'query_by'  : 'title, body',
  'query_by_weights': '1,1'
}))
