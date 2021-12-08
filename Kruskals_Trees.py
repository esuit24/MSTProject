#this algorithm implements Kruskal's with trees
import sys
from sys import argv
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

file = open(argv[1], "r")
lines = lines = file.readlines()
nums = lines[0].split()
numVertices = int(nums[0])
numEdges = int(nums[1])

edges = []
tree = []

for line in lines:
    if line is not lines[0] and line is not lines[-1]:
        l = line.split()
        e = Edge(l[0], l[1], l[2])
        edges.append(e)

parent = []

def makeSets(graph):
    for i in range(len(graph)-1):
        parent.append(i)

#find is used to find what set i and j are in, returns
#what the parent is of i
def find(i):
    #keep going through until you get to the node
    #where i is its own parent (root)
    while (parent[i] != i):
        i = parent[i]
    #return owner of set
    return i

def union(i,j):
    parent[i] = j

def main():
    makeSets(edges)
    quickSort(edges,0,len(edges)-1)
    #find each vertex
    for i in range(len(edges)-1):
        edge = edges[i]
        set1 = find(edge.v1) #find parents
        set2 = find(edge.v2) #find parents
        if (set1 != set2):
            union(set1, set2)
            tree.append(edges[i])
    #check:
    sum = 0
    for k in range(len(tree)):
        sum += tree[k].w
    print(sum)
main()
