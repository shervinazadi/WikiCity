html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
import requests
n = 0
link = "https://en.wikipedia.org/wiki/Facebook"
f = requests.get(link)

html_doc = f.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title.string)
print()

for link in soup.find_all('a'):
    LinkString = str(link.get('href'))

    if LinkString[:6]=='/wiki/':
        if LinkString[:11]!='/wiki/File:':
            if LinkString[:16]!='/wiki/Wikipedia:':
                if LinkString[:14]!='/wiki/Special:':
                    if LinkString[:11]!='/wiki/Help:':
                        if LinkString[:15]!='/wiki/Category:':
                            if LinkString[:13]!='/wiki/Portal:':
                                print(link.get('href'))
                                n += 1
print (n)
