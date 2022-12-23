# Advent of code 17
from aocutils import *
# Sample: 3068 and 1514285714288
# Actual: 3069 and 1523167155404

rocks = [((2,0),(3,0),(4,0),(5,0)),
    ((2,1),(3,1),(4,1),(3,2),(3,0)),
    ((2,0),(3,0),(4,0),(4,1),(4,2)),
    ((2,0),(2,1),(2,2),(2,3)),
    ((2,0),(3,0),(2,1),(3,1))]

highest = 0
highest1 = 0
i = 0
ri = 0
rilast = 0
heightfix = 0

# startrock, rock-id, bottom height
def startrock(id, h):
    return tuple([(x[0],x[1]+h) for x in rocks[id%5]])

# topmost return highest y-value
def topmost(rock):
    return max(list(zip(*rock))[1])

# moverock, rock, jetchar - return False if stuck, else new rock
# sets highest as a side effect when stuck
def moverock(rock, jetchar, rockspace, rocks, njets):
    global highest
    global highest1
    global i
    global ri
    global rilast
    global heightfix
    deltax = 1 if jetchar == ">" else -1
    r = [(x[0]+deltax,x[1]) for x in rock]
    rs = set(r)
    if rs.intersection(rockspace) or min(list(zip(*r))[0]) < 0 or max(list(zip(*r))[0]) > 6:
        # overlap with rock or edge, keep original rock
        r = rock
    rr = [(x[0], x[1]-1) for x in r]
    rs = set(rr)
    if rs.intersection(rockspace):
        # overlap with rock or floor, keep last rock
        tm = topmost(r)
        if tm > highest:
            highest = tm
        rockspace.update(set(r))   # add this rock to the rockspace
        retval = False
    else:
        retval = rr
    i += 1
    if i == njets*5:
        highest1 = highest
        rilast = ri
    elif i == njets*10:
        deltah = highest-highest1
        deltar = ri-rilast
        cyclestogo = (rocks-ri)//deltar
        heightfix = deltah*cyclestogo
        ri += cyclestogo*deltar

    return retval


def dec17(fname, rocks, partn):
    global highest
    global highest1
    global i
    global ri
    global heightfix
    jets = flistofstrings(fname)[0]
    jetsl = len(jets)
    i = 0
    rockspace = set([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)])  # set of stationary rock bits
    highest = 0
    highest1 = 0
    heightfix = 0

    ri = 0
    while ri < rocks:
        r = startrock(ri, highest+4)
        #print(f"Starting {ri%5} at {r}")
        while r := moverock(r, jets[i%jetsl], rockspace, rocks, jetsl):
            pass
        ri += 1
    highest += heightfix
    print(f"part {partn}: {highest}")


print("Sample")
dec17("dec17s.txt", 2022, 1)
print("Actual")
dec17("dec17.txt", 2022, 1)  
print("Sample")
dec17("dec17s.txt", 1000000000000, 2)
print("Actual")
dec17("dec17.txt", 1000000000000, 2)  
