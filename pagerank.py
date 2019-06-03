from numpy import linalg as la
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from randomnodenetwork import *
import math
import operator

#Creates a random generated 100 node network called random100Graph.
random100Graph = nx.MultiDiGraph()
createGraph(random100Graph, 100)

#Creates a random generated 50 node network called random50Graph.
random50Graph = nx.MultiDiGraph()
createGraph(random50Graph, 50)

#Creates an example 10 node graph that's generated manually.
exampleGraph = nx.MultiDiGraph() 
exampleGraph.add_nodes_from(['A','B','C','D','E','F','G','H','I','J'])
exampleGraph.add_edges_from([('A','C'),('A','J'),('A','G'),('A','H'),('B','A'),('B','D'),('B','E'),('B','F'),
('B','G'),('B','I'),('C','A'),('C','B'),('C','D'),('C','E'),('D','I'),('D','E'),('E','A'),('E','F'),
('F','A'),('F','B'),('F','J'),('G','C'),('G','F'),('G','H'),('G','I'),('I','D'),('I','H'),('J','I'),
('J','G'),('J','D')])

def plotGraph(x): #Function to plot our node network graph G.
    nx.draw_kamada_kawai(x)
    #nx.draw_networkx_labels(x,pos=nx.circular_layout(x))
    plt.show()

def powerIteration(vector, maxIteration, diff, transMatrix, matrix): #Our PageRank algorithm method.
	a = [(1/la.norm(vector))] #Assigns first index in the list. See report definition x.x for a0
	for i in range(1, maxIteration): #Our first break option, to make sure it won't go on to infinity.
		a.append((transMatrix * matrix)*a[i-1] / la.norm((transMatrix * matrix)*a[i-1])) #Adds every iteration into the end of the list, using the mathematical formula for the Power Method, see definition x.x in our report.
		if la.norm(a[i]-a[i-1]) < diff: #Checks for every iteration: breaks out of the for loop, if the difference between our current and last ireration is less than our diff (difference) parameter.  
			break
	print(-np.sort(-a[-1], axis = 0)) #Prints sorted output vector, which is our ranking / result.
	print(np.argsort(-a[-1], axis = 0)) #Prints the index the values came from, before sorted, now sorted.

def printComparer(maxIteration, diff, graph): #Method to print out the comparing built-in function of the PageRank algorithm from the NetworkX library.
	ranking = nx.pagerank_scipy(graph, alpha = 1, tol = diff, max_iter = maxIteration)
	sortedRanking = sorted(ranking.items(), key=operator.itemgetter(1))	
	print(sortedRanking)

def run(maxIteration, diff, graph): #Method that calls all our different methods for a specific graph chosen.
	A = nx.to_numpy_matrix(graph) #Taking the node network graph G and making it into a adjacency matrix A.
	transA = A.transpose() #Taking the adjacency matrix A and making it transposed.
	authVector = transA.sum(axis=1) #Summing rows of the transposed matrix into a vector
	powerIteration(authVector, maxIteration, diff, transA, A) 
	printComparer(maxIteration, diff, graph)
	plotGraph(graph)

run(10000, 0.0001, exampleGraph)