import pandas as pd
import networkx as nx
from networkx.readwrite import json_graph
import json
import csv

class ExtractLinks:

    def __init__(self, soup):

        ArticleList = []
        FileList = []
        WikiList = []
        SpecialList = []
        HelpList = []
        CategoryList = []
        PortalList = []
        OutsideList = []

        # Seperating different kinds of links

        for link in soup.find_all('a'):
            LinkString = str(link.get('href'))

            if LinkString[:6]=='/wiki/':

                if LinkString[:11]=='/wiki/File:':
                    FileList.append(link.get('href'))
                elif LinkString[:16]=='/wiki/Wikipedia:':
                    WikiList.append(link.get('href'))
                elif LinkString[:14]=='/wiki/Special:':
                    SpecialList.append(link.get('href'))
                elif LinkString[:11]=='/wiki/Help:':
                    HelpList.append(link.get('href'))
                elif LinkString[:15]=='/wiki/Category:':
                    CategoryList.append(link.get('href'))
                elif LinkString[:13]=='/wiki/Portal:':
                    PortalList.append(link.get('href'))
                else:
                    ArticleList.append(link.get('href'))
            else:
                OutsideList.append(link.get('href'))

        # Creating Panda Series out of lists

        self.Articles = pd.Series(ArticleList)
        self.Category = pd.Series(CategoryList)
        self.Files =  pd.Series(FileList)
        self.Wiki = pd.Series(WikiList)
        self.Special = pd.Series(SpecialList)
        self.Help = pd.Series(HelpList)
        self.Portal = pd.Series(PortalList)
        self.Outside = pd.Series(OutsideList)

        # Creating Panda DataFrames out of Series
        ''' 
        d = {'Articles' : pd.Series(ArticleList), 'Category' : pd.Series(CategoryList),
             'Files' : pd.Series(FileList), 'Wiki' : pd.Series(WikiList),
             'Special' : pd.Series(SpecialList), 'Help' : pd.Series(HelpList),
             'Portal' : pd.Series(PortalList), 'Outside' : pd.Series(OutsideList), }
    
        LinkDataFrame = pd.DataFrame(d)
        '''

class Graph:

    def __init__(self):
        self.Graph = nx.Graph()
        self.NodeName = []
        self.NameBasicNumber = 10000

    def Expander(self, LinkExtractedPage,i):
        CurrentNum = self.Graph.number_of_edges()
        for j, row in LinkExtractedPage.Articles.iteritems():

            if row[6:] not in self.Graph.nodes:
                self.Graph.add_node(CurrentNum + self.NameBasicNumber + j)
                self.Graph.add_edge(CurrentNum + self.NameBasicNumber + j, self.NameBasicNumber + i, value=1)
                self.NodeName.append([CurrentNum + self.NameBasicNumber + j,row[6:]])

            #nx.set_edge_attributes(self.Graph, 'weight', nx.get_edge_attributes(self.Graph, 'weight')[(row[6:], LinkName)] + 1)

    def JsonSaver(self):

        self.JsonData = json_graph.node_link_data(self.Graph)

        with open('D3 Visualizer/result.json', 'w') as fp:
            json.dump(self.JsonData, fp)

    def GefxSaver(self):
        nx.write_gexf(self.Graph, "Gephi Visualizer/GEFX/result.gexf")

    def CSVSaver(self):

        self.delimiter = ','

        self.EdgePath = 'Houdini Visualizer/CSV/edges.csv'
        self.NodePath = 'Houdini Visualizer/CSV/nodes.csv'

        self.EdgeCounter = 0
        self.NodeCounter = 0

        self.CsvEdge = list(self.Graph.edges())
        #print (self.CsvEdge)
        self.CsvNode =  self.Graph.nodes()
        print (self.CsvNode)

        with open(self.EdgePath, 'wt') as csvfile:     ## writing the whole deference phase
            writer = csv.writer(csvfile, delimiter=self.delimiter,
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for p in range(len(self.CsvEdge)):
                writer.writerow(self.CsvEdge[p])

                self.EdgeCounter = self.EdgeCounter + 1

        with open(self.NodePath, 'wt') as csvfile:     ## writing the whole deference phase
            writer = csv.writer(csvfile, delimiter=self.delimiter,
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for p in range(len(self.NodeName)):
                writer.writerow(self.NodeName[p])

                self.NodeCounter = self.NodeCounter + 1

