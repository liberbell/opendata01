# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224') as f:
    text = f.read()
    decodetext = text.decode('utf-8')
    print(textwrap.fill(decodetext, width=50))

print()

obj = json.loads(decodetext)
print(obj['kind'])

print(obj['items'][0]['kind'])
print(obj['items'][0]['searchInfo']['textSnippet'])
