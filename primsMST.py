import sys
from sys import argv
import numpy as np
import turtle as t
import math
import time
from graphics import *

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

def draw_edge(v1, v2): #this function draws an edeg from vertex v1 to vertex v2
    x1=740 # radius of 340 + 400 for the central x point on the screen
    y1=400 #this represents the central y point of the screen
    angle=(2*math.pi)/numVerticies #finds the angle between any two consecutive verticies
    h=math.sqrt((484**2)* (1-math.cos(angle*(1+v1)))) #heuristic value
    p1x=x1-h*math.sin(angle*(v1+1)/2)#x value of node 1
    p1y=y1+h*math.cos(angle*(v1+1)/2)#y value of node 1
    h=math.sqrt((484**2)* (1-math.cos(angle*(1+v2))))
    p2x=x1-h*math.sin(angle*(v2+1)/2)#x value of node 2
    p2y=y1+h*math.cos(angle*(v2+1)/2)#y value of node 2
    p1=Point(p1x,p1y)
    p2=Point(p2x,p2y)
    line=Line(p1,p2)#draws line
    #setWidth(1)
    return line

def compute_tree():
    win2=GraphWin("Table", 800, 800)
    x1=750# radius of 350 + 400 for the central x point on the screen
    y1=400#this represents the central y point of the screen
    angle=(2*math.pi)/numVerticies #finds the angle between any two consecutive verticies
    for i in range(numVerticies): #draws circles for vertices.
        h=math.sqrt((500**2)* (1-math.cos(angle*(1+i)) ) ) #heuristic value
        x2=x1-h*math.sin(angle*(i+1)/2) #x value of center of vertex
        y2=y1+h*math.cos(angle*(i+1)/2) #y value of center of vertex
        pt=Point(x2,y2)
        circ= Circle(pt, 12)
        label= Text(pt, str(i+1))
        circ.draw(win2)
        label.draw(win2)
    x1=750
    y1=400
    for i in range(numEdges): #draws edge
        v1=graph[i][0]
        v2=graph[i][1]
        line=draw_edge(v1,v2)
        line.draw(win2)
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
        for e in range(len(verticies_to_check)):
            if (verticies_to_check[e][0] in verticies_in_tree and
            verticies_to_check[e][2] < best_edge and verticies_to_check[e][1] not in verticies_in_tree):
            #also check if the other end of vertex is in tree already
            #v1 in tree, v2 not in tree
                best_edge = verticies_to_check[e][2]
                add_vertex = [verticies_to_check[e][0], verticies_to_check[e][1]]
                index = e
                line=draw_edge(verticies_to_check[e][0], verticies_to_check[e][1])
                line.setFill('cyan') #edge in cyan represents edge being processed
                line.draw(win2)
                line=draw_edge(verticies_to_check[e][0], verticies_to_check[e][1])
                time.sleep(0.2)
                line.setFill('black')
                line.draw(win2)
            elif (verticies_to_check[e][1] in verticies_in_tree and
            verticies_to_check[e][2] < best_edge and verticies_to_check[e][0] not in verticies_in_tree):
            #v2 in tree, v1 not in tree
                best_edge = verticies_to_check[e][2]
                add_vertex = [verticies_to_check[e][1], verticies_to_check[e][0]]
                index = e
                line=draw_edge(verticies_to_check[e][0], verticies_to_check[e][1])
                line.setFill('cyan') #edge in cyan represents edge being processed
                line.draw(win2)
                line=draw_edge(verticies_to_check[e][0], verticies_to_check[e][1])
                time.sleep(0.2)
                line.setFill('black')
                line.draw(win2)

                #find a vertex that makes an edge with starting vertex
        #add new vertex to list of verticies, remove from original
        #print("AV: x" + str(add_vertex[1]))
        verticies_in_tree.append(add_vertex[1])
        v1=add_vertex[0]
        v2=add_vertex[1]

        line=draw_edge(v1, v2)
        line.setFill('DeepPink') #pink edge represents edge in MST.
        line.draw(win2)
        #print("VIT2: " + str(verticies_in_tree))
        #print(index)
        verticies_to_check.pop(index)
        #add new edge to tree, remove from original
        edges_in_tree.append(best_edge)#already removed from graph

        #update data structure for finding edge
            #update pointers
        curr_v = add_vertex[1]
        parent[curr_v] = add_vertex[0]
        best_weight[curr_v] = best_edge #best edge
        #print("Best Weight: " + str(best_edge))
        weight += best_edge
    #print("Weight: " + str(weight))
    print("Weights: " + str(best_weight))
    print("edges: " + str(verticies_in_tree))
    print("Final Weight: " + str(weight))
    win2.getMouse()
    win2.close()
    return weight

compute_tree()
