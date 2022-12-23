# Advent of code 18
from aocutils import *
from collections import Counter
from re import compile
# Sample:  64 and 
# Actual:  3346 and 

def sides(c):
    return ((c[0],c[1],c[2]+0.5), 
        (c[0],c[1],c[2]-0.5),
        (c[0],c[1]+0.5,c[2]),
        (c[0],c[1]-0.5,c[2]),
        (c[0]+0.5,c[1],c[2]),
        (c[0]-0.5,c[1],c[2]))

def dec18(fname):
    faces = Counter()
    cubes = compile("(\d+),(\d+),(\d+)")
    cl = [(int(x.group(1)), int(x.group(2)), int(x.group(3))) for x in [cubes.search(x) for x in flistofstrings(fname)]]
    uzcl = list(zip(*cl))
    xmm = (min(uzcl[0]),max(uzcl[0]))
    ymm = (min(uzcl[1]),max(uzcl[1]))
    zmm = (min(uzcl[2]),max(uzcl[2]))
    print(xmm, ymm, zmm)
    for c in cl:
        faces.update(sides(c))
    nakedfaces = filter(lambda x: x[1] == 1, faces.items())
    print(f"part 1: {len(list(nakedfaces))}")
#    print(f"part 2: {len(sides)}")
 
print("Sample")
dec18("dec18s.txt")
print("Actual")
dec18("dec18.txt")
