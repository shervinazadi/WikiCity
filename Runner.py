from bs4 import BeautifulSoup
import requests
import Utilities

#Setting up the link

LinkName = "Social_networking_service"
link = "https://en.wikipedia.org/wiki/" + LinkName

#requesting and recieving the data from the link
f = requests.get(link)

#extracting the data in text format
html_doc = f.text

#parsing the text into a soup
soup = BeautifulSoup(html_doc, 'html.parser')

#printing the name of the page
print(soup.title.string)
print()

#extracting the links inside the page
TestLinks = Utilities.ExtractLinks(soup)

#initializing the graph
TestGraph = Utilities.Graph()

#using links to create new nodes and edges
TestGraph.Expander(TestLinks,LinkName)

print (TestGraph.Graph.edges)
print (TestGraph.Graph.number_of_edges())
