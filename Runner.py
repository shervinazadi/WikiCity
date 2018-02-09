from bs4 import BeautifulSoup
import requests
import Utilities
import time

millis = int(round(time.time() * 1000))

for i in range(20):

    #Setting up the link

    if i==0:
        LinkName = "/wiki/Social_networking_service"
    else:
        LinkName = TestLinks.Articles[i]

    link = "https://en.wikipedia.org" + LinkName
    #requesting and recieving the data from the link
    f = requests.get(link)

    #extracting the data in text format
    html_doc = f.text

    #parsing the text into a soup
    soup = BeautifulSoup(html_doc, 'html.parser')

    #printing the name of the page
    print()
    print(soup.title.string)

    #extracting the links inside the page
    TestLinks = Utilities.ExtractLinks(soup)

    if i==0:
        #initializing the graph
        TestGraph = Utilities.Graph()

    #using links to create new nodes and edges
    TestGraph.Expander(TestLinks,LinkName)

    #printing the time
    CurMillis = int(round(time.time() * 1000))
    print (CurMillis - millis)

#saving the result files
TestGraph.JsonSaver()
#TestGraph.CSVSaver()
TestGraph.GefxSaver()

#print (TestGraph.Graph.edges)
#print (TestGraph.Graph.number_of_edges())
