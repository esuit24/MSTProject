# n = |V|
# m = |E|

import sys
from sys import argv
import time
from graphics import *
import math

#class edge to store an edge and the two vertices it connects
#also stores the weight of each edge

class Edge:
    def __init__(self, vertexOne, vertexTwo, weight):
        self.v1 = vertexOne
        self.v2 = vertexTwo
        self.w = weight

    def print():
        print(v1 + " " + v2 + " " + w)

def quickSort(arr, low, high):
    if len(arr) == 1:
        print("returning")
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        #print("pi: " + str(pi))

        # sorts elements before partition
        quickSort(arr, low, pi - 1)

        # sorts elements after partition
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    # index of smaller element
    i = (low - 1)
    pivot = arr[high].w

    for j in range(low, high):

        # If current element is <= pivot
        if float(arr[j].w) <= float(pivot):
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return int(i + 1)

def find(sets, v1):
    for i in range(len(sets)):
        if int(v1) in sets[i]:
            return i

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
    return line

def draw_vertex(v1, numVertices): #draws a vertex
    x1=750# radius of 350 + 400 for the central x point on the screen
    y1=400#this represents the central y point of the screen
    angle=(2*math.pi)/numVertices #finds the angle between any two consecutive verticies
    h=math.sqrt((500**2)* (1-math.cos(angle*(1+v1))))
    x2=x1-h*math.sin(angle*(v1+1)/2)
    y2=y1+h*math.cos(angle*(v1+1)/2)
    pt=Point(x2,y2)
    circ= Circle(pt, 12)
    label= Text(pt, str(i+1))
    #label.draw(win2)
    return circ

#main function

file = open(argv[1], "r") #opens file
#saves file data as variable
lines = file.readlines()
#removes first line of file to get #vertices and #edges
nums = lines[0].split()
numVertices = int(nums[0])
numEdges = int(nums[1])

#increases recursion depth for quick sort

print("E: " + str(numEdges) + " V: " + str(numVertices))
sys.setrecursionlimit(3000)

globalMin = sys.maxsize
weightMST = 0
edges = []
#list of sets to which each vertex belongs
sets = []

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
    label= Text(pt, str(i+1)) #labels each node
    circ.draw(win2)
    label.draw(win2)


for line in lines: #processes file data into a list of edges
    if line is not lines[0] and line is not lines[-1]:
        l = line.split()
        e = Edge(l[0], l[1], l[2])
        edges.append(e)

for i in range(numEdges): #draws all edges in the graph
    v1=int(edges[i].v1)
    v2=int(edges[i].v2)
    line=draw_edge(v1,v2)
    line.draw(win2)

for i in range(numVertices):#initially, each vertex belongs to its own set
    sets.append({i})

print("Quick sorting")
quickSort(edges, 0, len(edges) - 1) #presorts edges from least to greatest

print("sorting complete")

for e in edges:
    first = int(find(sets, e.v1))#find(v1)
    second = int(find(sets, e.v2))#find(v2)
    circ1= draw_vertex(first, numVertices)
    circ2= draw_vertex(second, numVertices)
    circ2.setOutline("cyan")
    circ2.draw(win2) #draws nodes being processed in cyan
    circ1.setOutline("cyan")
    circ1.draw(win2) #draws nodes being processed in cyan

    if first != second: #ensures the set with the larger index is disappearing for consistency
        line=draw_edge(int(e.v1),int(e.v2))
        line.setFill('DeepPink')
        line.draw(win2) #draws MST in pink
        sets[first] = set.union(sets[first], sets[second])
        sets.pop(second)
        weightMST += float(e.w)
    time.sleep(0.5)
    circ1= draw_vertex(first, numVertices)
    circ2= draw_vertex(second, numVertices)
    #circ2.setFill("white")
    circ2.draw(win2)
    #circ1.setFill("white")
    circ1.draw(win2)
    #label1= Text(first, str(i+1))
    #label2= Text(second, str(i+1))


win2.getMouse()
win2.close()

print(weightMST)
