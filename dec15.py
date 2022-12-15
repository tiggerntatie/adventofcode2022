# Advent of code 15
from re import compile
from aocutils import *
# Sample:   and 
# Actual:   and  


def dec15(fname):
    ins = compile(".*=([\d\-]+).*=([\d\-]+).*=([\d\-]+).*=([\d\-]+)")
    ml = [[int(m.group(i)) for i in range(1,5)] for m in [ins.search(s) for s in flistofstrings(fname)]]
    print(ml)
    #print(f"part 1: {grains}")
    #print(f"part 2: {grains}")
 
print("Sample")
dec15("dec15s.txt")
#print("Actual")
#dec15("dec15.txt")
