# pcweb/tsclient.py
import typesense
import os

client = typesense.Client({
  'api_key': os.getenv("TYPESENSE_API_KEY"),
  'nodes': [{
    'host': '6xtoqsb1a4ip9u8gp-1.a1.typesense.net',
    'port': '443',
    'protocol': 'https'
  }],
  'connection_timeout_seconds': 2
})
