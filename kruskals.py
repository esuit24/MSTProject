# n = |V|
# m = |E|

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

        #if pi == 254:
        #    print("quicksorting")
        #    print(len(arr))
        #    for e in edges:
        #        print(e.w, end=", ") 
        #print("pi: " + str(pi))

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

file = open(argv[1], "r")
lines = file.readlines()
nums = lines[0].split()
numVertices = int(nums[0])
numEdges = int(nums[1])

print("E: " + str(numEdges) + " V: " + str(numVertices))
sys.setrecursionlimit(3000)

globalMin = sys.maxsize
weightMST = 0
edges = []
sets = []

for line in lines:
    if line is not lines[0] and line is not lines[-1]:
        l = line.split()
        e = Edge(l[0], l[1], l[2])
        edges.append(e)

for i in range(numVertices):
    sets.append({i})
    
print("Quick sorting")
quickSort(edges, 0, len(edges) - 1)
    
print("sorting complete")
  
for e in edges:
    first = int(find(sets, e.v1))
    second = int(find(sets, e.v2))

    #if second is None:
    #    print("EDGE INVALID: " + e.v1 + " " + e.v2)
    #    print(sets)
    
    #print(int(first))
    #print(int(second))
    
    if first != second:
        sets[first] = set.union(sets[first], sets[second])
        sets.pop(second)
        weightMST += float(e.w)
        
print(weightMST)