# Advent of code 18
from aocutils import *
from collections import Counter
from re import compile
# Sample:  64 and 58
# Actual:  3346 and 3178

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
    for c in cl:
        faces.update(sides(c))
    nakedfacescount = len(list(filter(lambda x: x[1] == 1, faces.items())))
    print(f"part 1: {nakedfacescount}")
    cset = set(cl)
    holefacecount = 0
    for x in range(xmm[0]+1, xmm[1]):
        for y in range(ymm[0]+1, ymm[1]):
            for z in range(zmm[0]+1, zmm[1]):
                if (x,y,z) not in cset:
                    if len(set([(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]).intersection(cset)) == 6:
                        holefacecount += 6
    print(f"part 2: {nakedfacescount - holefacecount}")
 
print("Sample")
dec18("dec18s.txt")
print("Actual")
dec18("dec18.txt")
