# Advent of code 16
from re import compile
from collections import Counter
from aocutils import *
# Sample: 1651 and 
# Actual: and 

#  best valve flow
def bvf(vd, startvalve, timeleft):
    print(f"{startvalve} {timeleft}")
    if timeleft <= 0:
        return 0
    if timeleft == 30:
        return 0
    v = vd[startvalve]
    t1 = []
    t2 = []
    if v[1]:    # valve already open, get times to other nodes
        t1 = [bvf(vd, xx, timeleft-1) for xx in v[2]]
    else:
        # assume opening valve: remaining flow for this valve plus the rest
        t2 = [v[0]*(timeleft-1) + bvf(vd, xx, timeleft-1) for xx in v[2]]
    return max(t1+t2)
     
# example input line
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
def dec16(fname):
    vd = {}
    valves = compile("Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
    # flow rate, open/closed, connected valve list
    for v in [valves.search(s) for s in flistofstrings(fname)]:
        vd[v.group(1)] = [int(v.group(2)), 0, v.group(3).split(', ')]
    totflow = bvf(vd, 'AA', 30)
    print(f"part 1: {totflow}")

    #print(f"part 2: {tfreq}")


print("Sample")
dec16("dec16s.txt")
#print("Actual")
#dec16("dec16.txt")  
