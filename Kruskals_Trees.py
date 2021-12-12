#this algorithm implements Kruskal's with trees
import sys
from sys import argv

#initialize edge class
class Edge:
    #edge has 2 vertex attributes and a weight
    def __init__(self, vertexOne, vertexTwo, weight):
        self.v1 = vertexOne
        self.v2 = vertexTwo
        self.w = weight

    def print():
        print(v1 + " " + v2 + " " + w)

#quick sort: sorts elements in array arr recursively
#given indicies of first and last elements to be sorted
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

#takes in array, arr, to be partitioned and
#indicies that correspond to first and last elements
#to be partitioned
#returns the index to partition at
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

#file read in
file = open(argv[1], "r")
lines = lines = file.readlines()
nums = lines[0].split()
numVertices = int(nums[0])
numEdges = int(nums[1])

#set empty list of edges and verticies of tree
edges = []
tree = []

for line in lines:
    if line is not lines[0] and line is not lines[-1]:
        l = line.split()
        e = Edge(int(l[0]), int(l[1]), float(l[2]))
        edges.append(e)
#sets parent array to hold parent of each vertex
#in tree
parent = []

#initializes parent of each vertex to itself
def makeSets(graph):
    for i in range(len(graph)-1):
        parent.append(i)

#takes in vertex as input
#returns the parent of a given vertex i
def find(i):
    #iterates through until gets to the node
    #where i is its own parent (root)
    while (parent[i] != i):
        i = parent[i]
    #return owner of set
    return i

#takes in names of set owners to be unioned
#unions sets by assigning parent of one to parent of
#other
def union(i,j):
    parent[i] = j

#main method
def main():
    makeSets(edges)
    quickSort(edges,0,len(edges)-1)
    #iterates through edges in tree in sorted order
    for i in range(len(edges)-1):
        edge = edges[i]
        set1 = find(edge.v1) #find parents
        set2 = find(edge.v2) #find parents
        if (set1 != set2): #add to tree if not in cycle
            union(set1, set2)
            tree.append(edges[i])
    #sum total weight
    sum = 0
    for k in range(len(tree)):
        sum += tree[k].w
    #print final weight
    print(sum)
#execute algorithm
main()
