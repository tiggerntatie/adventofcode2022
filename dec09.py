# Advent of code 09
from aocutils import *
from re import compile
# Sample:  13 and 1 (Sample 2 is 88 and 36)
# Actual:  6190 and 2516

deltas = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

moveit = lambda p, m: [p[n]+m[n] for n in (0,1)]

def printvisited(v):
    xmin = 999
    xmax = -999
    ymin = 999
    ymax = -999
    for c in v:
        if c[0] < xmin:
            xmin = c[0]
        if c[0] > xmax:
            xmax = c[0]
        if c[1] < ymin:
            ymin = c[1]
        if c[1] > ymax:
            ymax = c[1]
    for y in range(ymin, ymax+1):
        print("".join(["#" if (x,y) in v else "." for x in range(xmin, xmax+1)]))

def dec09(fname):
    mpat = compile("([UDLR]) (\d+)")
    moves = []
    knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    visitedk1 = set([knots[1]])
    visitedk9 = set([knots[9]])
    for move in flistofstrings(fname):
        m = mpat.search(move)
        moves.append((m.group(1), int(m.group(2))))
    for m in moves:
        for _ in range(m[1]):
            knots[0] = moveit(knots[0], deltas[m[0]])
            for k in range(1,10):
                xdiff = knots[k-1][0]-knots[k][0]
                ydiff = knots[k-1][1]-knots[k][1]
                if abs(xdiff) > 1 and abs(ydiff) > 1:  # diagonal, two spaces!
                    knots[k] = (knots[k][0] + xdiff//2, knots[k][1] + ydiff//2)
                else:
                    if abs(xdiff) > 1:    # need to move tail horiz.
                        knots[k] = (knots[k][0] + xdiff//2, knots[k-1][1])
                    elif abs(ydiff) > 1:  # need to move tail vert.
                        knots[k] = (knots[k-1][0], knots[k][1] + ydiff//2)
            visitedk1.update([knots[1]])
            visitedk9.update([knots[9]])
    print(f"part 1: {len(visitedk1)}")
    print(f"part 2: {len(visitedk9)}")
 
print("Sample")
dec09("dec09s.txt")
print("Sample 2")
dec09("dec09s2.txt")
print("Actual")
dec09("dec09.txt")