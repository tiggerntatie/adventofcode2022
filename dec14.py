# Advent of code 14
from aocutils import *
#from re import compile
# Sample:  24 and 
# Actual:   and 

# series of integers from start to end
def rangeupdown(start, end):
    step = 1 if end > start else -1
    return range(start, end+step, step)

def dec14(fname):
    sld = {}
    for path in flistofstrings(fname):
        steps = [[int(y) for y in x.split(',')] for x in path.split(' -> ')]
        for i in range(len(steps)-1):
            for x in rangeupdown(steps[i][0],steps[i+1][0]):
                for y in rangeupdown(steps[i][1],steps[i+1][1])
                    sld[(x,y)] = '#'
                    print(x,y)
        print(steps)
    #print(f"part 1: {len(visitedk1)}")
    #print(f"part 2: {len(visitedk9)}")
 
print("Sample")
dec14("dec14s.txt")
#print("Actual")
#dec14("dec14.txt")