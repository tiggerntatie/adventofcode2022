# Advent of code 18
from aocutils import *
from re import compile
# Sample:  64 and 
# Actual:   and 

def sides(c):
    return ((c[0],c[1],c[2]+0.5))

def dec18(fname):
    cubes = compile("(\d+),(\d+),(\d+)")
    cl = [(int(x.group(1)), int(x.group(2)), int(x.group(3))) for x in [cubes.search(x) for x in flistofstrings(fname)]]
    print(cl)
#    print(f"part 1: {len(sides)}")
#    print(f"part 2: {len(sides)}")
 
print("Sample")
dec18("dec18s.txt")
#print("Actual")
#dec18("dec18.txt")
