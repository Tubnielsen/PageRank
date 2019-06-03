import numpy as np
import networkx as nx 
import random
import math

def graphName(integerValue): #Assigns different char names for each individual node.
    return str(0 + integerValue)

def createGraph(graph, nodeSum): #Calls our helper methods makeNodes and connectGraph to make a graph
    startNodes = nodeSum
    makeNodes(graph, startNodes)
    connectGraph(graph, startNodes)
    return graph

def randomPick(startNodes): #Helper to return a random int ranging from 0 to startNodes value.
    return random.randint(0, startNodes)

def connectGraph(graph, startNodes): #Helper method: adds edges (references) between nodes.
    for index_node in range(0, startNodes -1):
        for i in range(0, random.randint(0,8)): 
            temp = graphName(randomPick(startNodes))
            if temp != index_node:
                graph.add_edges_from( [(graphName(index_node), temp)] )

def makeNodes(graph, startNodes): #Helper method: adds startNodes number of nodes to our graph.
    for i in range(0, startNodes):
        graph.add_nodes_from(graphName(i))
