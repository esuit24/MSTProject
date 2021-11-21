#Implements Prim's algorithm with lists
import sys
from sys import argv
import numpy as np




file = open(argv[1], "r")
lines = file.readlines()
nums = lines[0].split()
numVerticies = int(nums[0])
print("NUM: " + str(numVerticies))
numEdges = int(nums[1])
graph = []
for line in lines:
    if line is not lines[0] and line is not lines[-1]:
        l = line.split()
        val = [int(l[0]), int(l[1]), float(l[2])]
        graph.append(val)
print(graph)
#storing the graph: list of vertex tuples, list of edge weights
parent = np.zeros((numVerticies,))
best_weight = np.zeros((numVerticies,))
starting_vertex = graph[0][0]
for i in range(numVerticies):
    parent[i] = starting_vertex
    best_weight[i] = float('inf')
print(numVerticies)


def compute_tree():
    #set tree as empty
    verticies_in_tree = []
    edges_in_tree = []
    verticies_to_check = graph
    print("Length: " + str(len(verticies_to_check)))
    weight = 0
    verticies_in_tree = [0]
    #set initial starting vertex
    for i in range(numVerticies-1): #add verticies-1 edges to tree
        #pick min cost edge between vertex in tree and vertex not in tree
        #print("print")
        best_edge = float('inf')
        add_vertex = (None, None)
        index = None
        #print("curr v: " + str(i))
        #print("VIT: " + str(verticies_in_tree))
        #print("Length of Check: " + str(len(verticies_to_check)))
        for e in range(len(verticies_to_check)):
            #print("Vertex to check: " + str(verticies_to_check[e]))
            #switch away from starting_vertex to any vertex in V
            #print("VTCL: " + str(verticies_to_check[e][2]))
            #print("Verticies Available: " + str(verticies_to_check[e][0]))
            #print("Verticies in tree: " + str(verticies_in_tree))
            #print("Index: " + str(e))
            if (verticies_to_check[e][0] in verticies_in_tree and
            verticies_to_check[e][2] < best_edge and verticies_to_check[e][1] not in verticies_in_tree):
            #also check if the other end of vertex is in tree already
                #print("VTC: " + str(verticies_to_check[e][2]))
                #print("Best Edge: " + str(best_edge))
                best_edge = verticies_to_check[e][2]
                add_vertex = [verticies_to_check[e][0], verticies_to_check[e][1]]
                index = e
                #print("BE: " + str(best_edge))
            elif (verticies_to_check[e][1] in verticies_in_tree and
            verticies_to_check[e][2] < best_edge and verticies_to_check[e][0] not in verticies_in_tree):
                best_edge = verticies_to_check[e][2]
                add_vertex = [verticies_to_check[e][1], verticies_to_check[e][0]]
                index = e

                #find a vertex that makes an edge with starting vertex
        #add new vertex to list of verticies, remove from original
        #print("AV: " + str(add_vertex[1]))
        verticies_in_tree.append(add_vertex[1])
        #print("VIT2: " + str(verticies_in_tree))
        #print(index)
        verticies_to_check.pop(index)
        #add new edge to tree, remove from original
        edges_in_tree.append(best_edge)#already removed from graph

        #update data structure for finding edge
            #update pointers
        curr_v = add_vertex[1]
        parent[curr_v] = add_vertex[0]
        best_weight[curr_v] = best_edge
        #print("Best Weight: " + str(best_edge))
        weight += best_edge
    #print("Weight: " + str(weight))
    print("Weights: " + str(best_weight))
    print("edges: " + str(verticies_in_tree))
    print("Final Weight: " + str(weight))
    return weight



compute_tree()
