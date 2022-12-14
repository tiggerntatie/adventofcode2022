# Advent of code 14
from aocutils import *
#from re import compile
# Sample:  24 and 
# Actual:   and 


def dec14(fname):
    sld = {}
    for path in flistofstrings(fname):
        print("path")
        for step in path.split(' -> '):
            print(step)
    #print(f"part 1: {len(visitedk1)}")
    #print(f"part 2: {len(visitedk9)}")
 
print("Sample")
dec14("dec14s.txt")
#print("Actual")
#dec14("dec14.txt")