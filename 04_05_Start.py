# HTML Parser Module
from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print('Start tag: ', tag)
        for attr in attr:
            print('attr: ', attr)

    def handle_endtag(self, tag):
        print('End tag: ', tag)

    def handle_comments(self, data):
        print('Comments: ', data)
    def handle_data(self, data):
        print('Data: ', data)

parser = HTMLParser()
parser.feed('<html><head><code></title></head><body><h1><!--hi-->I am a code</h1></body></html>')
print()
