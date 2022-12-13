# Advent of code 12
from aocutils import *
from re import compile
# Sample:  31 and 
# Actual:   and 

nodes = {}
unvisited = []

def sortunvisited():
    unvisited.sort(key = lambda x: nodes[x])

def dec12(fname):
    map = flistofstrings(fname)
    for x in range(len(map[0])):
        for y in range(len(map)):
            node = (x,y)
            nodes[node] = 1000000    # infinite distance
            unvisited.append(node)
    
    print(f"part 2: {top2[0]*top2[1]}")

print("Sample")
dec12("dec12s.txt")
print("Actual")
#dec12("dec12.txt")
