# Advent of code 16
from re import compile
from collections import Counter
from aocutils import *
# Sample: 1651 and 
# Actual: and 

def bestvalveflow(vd, startvalve, timeleft):
    if not timeleft:
        return 0
    if 
     
# example input line
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
def dec16(fname):
    vd = {}
    valves = compile("Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
    # flow rate, open/closed, connected valve list
    for v in [valves.search(s) for s in flistofstrings(fname)]:
        vd[v.group(1)] = [int(v.group(2)), 0, v.group(3).split(', ')]
    flowrate = bestvalveflow(vd, 'AA', 30)
    #print(f"part 1: {count}")

    #print(f"part 2: {tfreq}")


print("Sample")
dec16("dec16s.txt")
#print("Actual")
#dec16("dec16.txt")  
