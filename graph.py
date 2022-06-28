#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:50:52 2021

@author: raviravindran
"""

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' +self.dest.getName()
    
class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges={}
        
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node]=[]
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    
    def getNodeList(self):
        return self.edges
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName()+'->'\
                    +dest.getName()+'\n'
        return result[:-1]
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path)-1:
            result = result + '->'
    return result


def DFSAlgo(graph, start, end, path, shortest, toPrint=False):
    nodesListToVisit=[]
    visitedList = []
    nodesListToVisit.append(start)
    cost={}
    prev={}
    
    for nodes in graph.getNodeList():
        if nodes == start:
            cost[nodes]=0
            prev[nodes]="None"
        else:
            cost[nodes]=99999
            prev[nodes]="Empty"
    
    while len(nodesListToVisit) != 0:
        topElement = nodesListToVisit.pop(len(nodesListToVisit)-1)
        visitedList.append(topElement)
        #Check all children
        for node in graph.childrenOf(topElement):
            if node in visitedList:
                print("Node ", node.getName(), " already visited ")
                continue
            else:
                visitedList.append(node)
                cost[node] = cost[topElement] + 1
                print("Exploring Node:",node.getName(), ", Hops from Src ",cost[node])
                nodesListToVisit.append(node)
                prev[node] = topElement.getName();
                if node==end:
                    print("Destination updated with cost", cost[node])
    currNode = end
    shortest=[]
    
    if prev[currNode]=="Empty":
        print("No Path Found")
    else:
        shortest.append(currNode.getName())
        while prev[currNode] != "None":
            print("Curr Node and Prev Node: ", currNode.getName(), prev[currNode])
            tempNode = graph.getNode(prev[currNode])
            shortest.append(tempNode.getName())
            currNode = tempNode
        
        temppath=''
        
        shortest.reverse();
        for i in range(len(shortest)):
            temppath = temppath +shortest[i]
            if i!=(len(shortest)-1):
                temppath = temppath+ "->"
        print(temppath)
    
    return shortest
         
        


def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Current DFS Path: ', printPath(path))
    if start==end:
        return path
    for node in graph.childrenOf(start):
        print("Exploring Child ",node.getName())
        if node not in path :
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    DFSAlgo(graph, start, end, [], None, toPrint)
    print('')
    return DFS(graph, start, end, [], None, toPrint)

def buildCityGraph(graphType):
    g=graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver',
                 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g

def testSP(source, destination):
    g = buildCityGraph(Graph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    
    if sp!=None:
        print('Shortest path from ', source, 'to', destination, 'is', 
              printPath(sp))
    else:
        print("There is no path from", source, 'to', destination)


def calculateStandardDeviation(X):
    mean = sum(X)/len(X)
    sumsq=0
    for val in X:
        sumsq = sumsq+ (val - mean)**2
    
    variance = sumsq/len(X)
    stdDeviation = variance**0.5
    
    return stdDeviation


def main():
    testSP('Chicago', 'Boston')
    print('')
    testSP('Boston', 'Phoenix')
    
    X=[1,2,3,4,5,6,199,1000,2000]
    print("Std Deviation is : ", calculateStandardDeviation(X))
    

    
if __name__ == "__main__":
   main()