# Advent of code 12
from aocutils import *
# Sample:  31 and 29
# Actual:  497 and 492

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

def getpossibleneighbors(n, width, height, part):
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
        if part == 1:
            if p <= nheight+1:
                veryposs.append(nn)
        else:
            if p >= nheight-1:
                veryposs.append(nn)
    return veryposs

# implementations of Dijkstra's algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
def dec12(fname):
    global map, unvisited
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
        for p in getpossibleneighbors(current, width, height, 1):
            if nodes[p] > currdist + 1:
                nodes[p] = currdist + 1
        unvisited.pop(unvisited.index(current))
        sortunvisited()
        if current == end:
            break
        current = unvisited[0]
    print(f"part 1: {nodes[current]}")
    # process backwards
    unvisited = []
    for x in range(len(map[0])):
        for y in range(len(map)):
            node = (x,y)
            nodes[node] = 1000000    # infinite distance
            unvisited.append(node)
    start = end
    nodes[start] = 0
    width = x
    height = y
    sortunvisited()
    current = start
    found = False
    while not found:
        currdist = nodes[current]
        for p in getpossibleneighbors(current, width, height, 2):
            if nodes[p] > currdist + 1:
                nodes[p] = currdist + 1
        unvisited.pop(unvisited.index(current))
        sortunvisited()
        if getaltc(current) == 'a': # found an a!
            break
        current = unvisited[0]
    print(f"part 2: {nodes[current]}")


print("Sample")
dec12("dec12s.txt")
print("Actual")
dec12("dec12.txt")
