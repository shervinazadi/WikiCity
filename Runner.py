from bs4 import BeautifulSoup
import requests
import Utilities
import time

millis = int(round(time.time() * 1000))

#start of initiator for hierarchial explorer
#Setting up the link
LinkName = "/wiki/Social_networking_service"


link = "https://en.wikipedia.org" + LinkName
#requesting and recieving the data from the link
f = requests.get(link)

#extracting the data in text format
html_doc = f.text

#parsing the text into a soup
soup = BeautifulSoup(html_doc, 'html.parser')

#extracting the links inside the page
FirstTestLinks = Utilities.ExtractLinks(soup)
#end of initiator for hierarchial explorer

for i in range(4):

    #Setting up the link

    if i==0:
        LinkName = "/wiki/Social_networking_service"
    else:
        LinkName = FirstTestLinks.Articles[i]

    link = "https://en.wikipedia.org" + LinkName
    #requesting and recieving the data from the link
    f = requests.get(link)

    #extracting the data in text format
    html_doc = f.text

    #parsing the text into a soup
    soup = BeautifulSoup(html_doc, 'html.parser')

    #printing the name of the page
    print()
    print ('Page Number : ' + str(i) + ' :')
    print('Page Name : ' + str(soup.title.string))

    #extracting the links inside the page
    TestLinks = Utilities.ExtractLinks(soup)

    if i==0:
        #initializing the graph
        TestGraph = Utilities.Graph()

    #using links to create new nodes and edges
    TestGraph.Expander(TestLinks,i)

    #printing the time
    CurMillis = int(round(time.time() * 1000))
    print ('Elapsed Time : ' + str((CurMillis - millis)/1000))

#saving the result files
TestGraph.JsonSaver()
TestGraph.CSVSaver()
TestGraph.GefxSaver()

#print (TestGraph.Graph.edges)
#print (TestGraph.Graph.number_of_edges())
