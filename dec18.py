# Advent of code 18
from aocutils import *
from re import compile
# Sample:  64 and 
# Actual:   and 

def dec18(fname):
    cubes = compile("(\d+),(\d+),(\d+)")
    cl = [x.group(1), x.group(2), x.group(3) for x in [cubes.search(x) for x in flistofstrings(fname)]]
    print(cl)
#    print(f"part 1: {len(sides)}")
#    print(f"part 2: {len(sides)}")
 
print("Sample")
dec18("dec18s.txt")
#print("Actual")
#dec18("dec18.txt")
