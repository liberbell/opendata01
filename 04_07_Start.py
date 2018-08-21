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

input1 = input('Put in the First Tag: ')
input2 = input('Put in the Second Tag: ')
# input3 = input('Put in the HTML code')

print(input1)
print(obj[input1][0][input2])
