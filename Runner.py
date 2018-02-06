from bs4 import BeautifulSoup
import requests
import Utilities






for i in range(3):

    #Setting up the link

    if i==0:
        LinkName = "/wiki/Social_networking_service"
    else:
        LinkName = TestLinks.Articles[1]

    link = "https://en.wikipedia.org" + LinkName
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

    if i==0:
        #initializing the graph
        TestGraph = Utilities.Graph()

    #using links to create new nodes and edges
    TestGraph.Expander(TestLinks,LinkName)

#saving the json file
TestGraph.JsonSaver()

print (TestGraph.Graph.edges)
print (TestGraph.Graph.number_of_edges())
