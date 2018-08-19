# HTML Parser Module
from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print('Start tag: ', tag)
        for attr in attr:
            print('attr: ', attr)

    def handle_endtag(self, tag):
        print('End tag: ', tag)

    def handle_comment(self, data):
        print('Comment: ', data)
    def handle_data(self, data):
        print('Data: ', data)

parser = HTMLParser()
parser.feed('<html><head><code></title></head><body><h1><!--hi-->I am a code</h1></body></html>')
print()

input = input('Put in the HTML code')
parser.feed(input)
print()

htmlFile = open('samHTML.html', 'r')
s = ''
for line in htmlFile:
    s += line
parser.feed(s)
