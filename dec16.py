# Advent of code 16
from re import compile
from aocutils import *
from functools import cache
# Sample: 1651 and 
# Actual: and 
# This is not a working solution. It will solve the sample, but takes too long on the actual data set. 
# This might be made to work by pruning paths that contain zero-flow valves, but this is proving
# to be a significant problem on its own! So I will leave this as a work in progress for the time being!


#  best valve flow (state, topology dict, id->name, name->id)
#  st = bvf(st, top, topid_n, topn_id)
def bvf(st, top, idn, nid):

    # newstate from oldstate and deltat
    def newstate(st, dt):
        return (st[0], st[1]+dt, st[2]+sum([top[idn[i]][0]*dt*st[3][i] for (i,o) in enumerate(st[3])]), st[3])
    
    # branchstate from oldstate and new root [name,distance], advancing time by one tick
    def branchstate(st, rootnamet):
        travelst = newstate(st, rootnamet[1])
        return (nid[rootnamet[0]],)+travelst[1:4]

    # locals
    usablevalves = sum([top[n][0]!=0 for n in top])
    timeavailable = 30

    # inner function - recursive and memoized
    @cache
    def bvfr(st):
        #print(f"entering bvfr: {st}")
        if sum(st[3]) == usablevalves:
            # all valves open that can be used.. race to end
            return newstate(st, timeavailable-st[1])[2]  # return total flow
        if st[1] == timeavailable:
            # time's up
            return st[2]    # total flow
        if st[1] == timeavailable - 1:
            # one tick left
            return newstate(st, 1)[2] # total flow
        outcomes = []
        thisid = st[0]
        rootflowrate = top[idn[st[0]]][0]
        if  rootflowrate != 0 and not st[3][st[0]]:
            # valve is off.. try turning on valve
            nextst = newstate(st, 1)
            nextst = nextst[:3]+(nextst[3][:thisid]+(1,)+nextst[3][thisid+1:],)
            #print(f"turning on valve {nextst[0]} new state: {nextst}")
            for nt in top[idn[thisid]][1]:   # connected nodes
                outcomes.append(bvfr(branchstate(nextst, nt)))
        # just try going to connected nodes
        for nt in top[idn[thisid]][1]:       # connected nodes
            outcomes.append(bvfr(branchstate(st, nt)))
        if len(outcomes):
            return max(outcomes)
        return 0
    
    return bvfr(st)

# example input line
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
def dec16(fname):
    top = {}
    valves = compile("Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
    # two pieces of information: 
    # 1) Topology: the flow rate and connection graph. A dictionary with valve name keys.
    # each connected valve is a name and distance (default 1)
    for v in [valves.search(s) for s in flistofstrings(fname)]:
        top[v.group(1)] = [int(v.group(2)), [[n,1] for n in v.group(3).split(', ')]]

    # an id -> name map, topn_id
    # a name -> id map, topid_n
    topn_id = {}
    topid_n = [0]*len(top)
    for (i, vn) in enumerate(sorted(top)):
        topid_n[i] = vn
        topn_id[vn] = i
    # 2) State: root valve id, the clock, total flow, open/closed list (sorted by name) - this can be used to memoize
    st = (topn_id['AA'], 0, 0, tuple([0] * len(top)))
    #print(st)
    maxflow = bvf(st, top, topid_n, topn_id)
    print(f"part 1: {maxflow}")

    #print(f"part 2: {tfreq}")


print("Sample")
dec16("dec16s.txt")
#print("Actual")
#dec16("dec16.txt")  
