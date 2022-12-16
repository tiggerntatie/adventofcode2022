# Advent of code 16
from re import compile
from collections import Counter
from aocutils import *
# Sample: 1651 and 
# Actual: and 

     
# example input line
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
def dec16(fname):
    vd = {}
    valves = compile("Valve () has flow rate=([\d]+]); tunnels? lead to valves? (.+)")
    #ml = [[int(m.group(i)) for i in range(1,5)] for m in [valvessearch(s) for s in flistofstrings(fname)]]
    for v in [valves.search(s) for s in flistofstrings(fname)]]:
        vd[v.group(1)] = [int(v.group(2)), v.group(3).split(',')]
    print(vd)
    #print(f"part 1: {count}")

    #print(f"part 2: {tfreq}")


print("Sample")
dec16("dec16s.txt")
#print("Actual")
#dec16("dec16.txt")  
