from bs4 import BeautifulSoup
import requests
import Utilities

n = 0
link = "https://en.wikipedia.org/wiki/Facebook"
f = requests.get(link)

html_doc = f.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title.string)
print()

TestLinks = Utilities.ExtractLinks(soup)
print(TestLinks)
