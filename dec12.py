# Advent of code 12
from aocutils import *
from re import compile
# Sample:  31 and 
# Actual:   and 

nodes = {}
unvisited = []
map = None

def sortunvisited():
    unvisited.sort(key = lambda x: nodes[x])

def getaltc(n):
    c = map[n[1]][n[0]]
    if c == 'S':
        c = 'a'
    elif c == 'E':
        c = 'z'
    return c

def getpossibleneighbors(n, width, height):
    poss = []
    veryposs = []
    if n[0] < width:
        poss.append((n[0]+1,n[1]))  # neighbor to right
    if n[0] > 0:
        poss.append((n[0]-1,n[1]))  # neighbor to left
    if n[1] < height:
        poss.append((n[0],n[1]+1))  # neighbor to lower
    if n[1] > 0:
        poss.append((n[0],n[1]-1))  # neighbor to upper
    nheight = ord(getaltc(n))
    for (nn, p) in [(x, ord(getaltc(x))) for x in poss]:
        if p <= nheight+1:
            veryposs.append(nn)
    return veryposs

def dec12(fname):
    global map
    start = None
    end = None
    map = flistofstrings(fname)
    current = None
    for (n, l) in enumerate(map):
        if 'S' in l:
            start = (l.find('S'), n)
        if 'E' in l:
            end = (l.find('E'), n)
        if start and end:
            break
        
    for x in range(len(map[0])):
        for y in range(len(map)):
            node = (x,y)
            nodes[node] = 1000000    # infinite distance
            unvisited.append(node)
    nodes[start] = 0
    width = x
    height = y
    sortunvisited()
    current = start
    found = False
    while not found:
        currdist = nodes[current]
        for p in getpossibleneighbors(current, width, height):
            if nodes[p] > currdist + 1:
                nodes[p] = currdist + 1
        unvisited.pop(unvisited.index(current))
        sortunvisited()
        if current == end:
            break
        current = unvisited[0]
        
    print(f"part 1: {nodes[current]}")

print("Sample")
dec12("dec12s.txt")
print("Actual")
dec12("dec12.txt")
