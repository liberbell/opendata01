# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224') as f:
    text = f.read()
    decodetext = text.decode(UTF-8)
    print(textwrap.fill(decodetext, width=50))
