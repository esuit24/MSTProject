#Implements Prim's algorithm with lists
import sys
from sys import argv
import numpy as np

#read in files
file = open(argv[1], "r")
lines = file.readlines()
nums = lines[0].split()
numVerticies = int(nums[0])
#holds vertex and edge information from file
numEdges = int(nums[1])
graph = []
#add information to array data structure from file
for line in lines:
    if line is not lines[0] and line is not lines[-1]:
        l = line.split()
        val = [int(l[0]), int(l[1]), float(l[2])]
        graph.append(val)

parent = np.zeros((numVerticies,))
best_weight = np.zeros((numVerticies,))
starting_vertex = graph[0][0]
for i in range(numVerticies):
    parent[i] = starting_vertex
    best_weight[i] = float('inf')


def compute_tree():
    #set tree as empty
    #set data structures to store edge and verticies in tree
    verticies_in_tree = []
    edges_in_tree = []
    verticies_to_check = graph
    #weight of MST
    weight = 0
    verticies_in_tree = [0]
    #set initial starting vertex
    for i in range(numVerticies-1): #add verticies-1 edges to tree
        #pick min cost edge between vertex in tree and vertex not in tree
        best_edge = float('inf')
        #initialize vertex to add to tree
        add_vertex = (None, None)
        #initialize index of vertex added to tree
        index = None
        for e in range(len(verticies_to_check)):
        #if v1 in tree, v2 not in tree
            if (verticies_to_check[e][0] in verticies_in_tree and
            verticies_to_check[e][2] < best_edge and verticies_to_check[e][1] not in verticies_in_tree):
            #if v1 in tree, v2 not in tree
                best_edge = verticies_to_check[e][2] #set as new best edge seen
                add_vertex = [verticies_to_check[e][0], verticies_to_check[e][1]]#set vertex pair to be added in the form (parent, new vertex)
                index = e #set index of vertex/edge added to tree
            elif (verticies_to_check[e][1] in verticies_in_tree and
            verticies_to_check[e][2] < best_edge and verticies_to_check[e][0] not in verticies_in_tree):
            #if v2 in tree, v1 not in tree
                best_edge = verticies_to_check[e][2] #set as new best edge seen
                add_vertex = [verticies_to_check[e][1], verticies_to_check[e][0]] #set vertex pair to be added in the form (parent, new vertex)
                index = e #set index of vertex/edge added to tree

        #add new vertex to list of verticies, remove from original
        verticies_in_tree.append(add_vertex[1])
        verticies_to_check.pop(index)
        #add new edge to tree
        edges_in_tree.append(best_edge)

        #update data structure for finding edge
        #update pointers
        curr_v = add_vertex[1]
        parent[curr_v] = add_vertex[0]
        best_weight[curr_v] = best_edge

        weight += best_edge

    print("edges: " + str(verticies_in_tree))
    print("Final Weight: " + str(weight))
    return weight



compute_tree()
