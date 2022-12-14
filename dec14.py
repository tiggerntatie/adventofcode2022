# Advent of code 14
from aocutils import *
#from re import compile
# Sample:  24 and 
# Actual:   and 

# series of integers from start to end
def rangeupdown(start, end):
    step = 1 if end > start else -1
    return range(start, end+step, step)

# run a sand grain down
# sld is the slice map
# pos is the grain position (x,y) tuple
# bottom is the lowest piece of rock y coord
# returns True if grain can't move further
# returns False if grain falls below the bottom
def sandstep(sld, pos, bottom):
    if pos[1] == bottom:
        # freefall now
        return False
    if (pos[0],pos[1]+1) in sld:
        if (pos[0]-1,pos[1]+1) in sld:
            if (pos[0]+1,pos[1]+1) in sld:
                # can't move
                sld[pos] = 'o'
                return True
            else:
                return sandstep(sld, (pos[0]+1,pos[1]+1), bottom)
        else:
            return sandstep(sld, (pos[0]-1,pos[1]+1), bottom)
    else:
        return sandstep(sld, (pos[0],pos[1]+1), bottom)

def dec14(fname):
    sld = {}
    lowestrock = 0
    for path in flistofstrings(fname):
        steps = [[int(y) for y in x.split(',')] for x in path.split(' -> ')]
        for i in range(len(steps)-1):
            for x in rangeupdown(steps[i][0],steps[i+1][0]):
                for y in rangeupdown(steps[i][1],steps[i+1][1]):
                    sld[(x,y)] = '#'
                    if y > lowestrock:
                        lowestrock = y
    grains = 0
    while sandstep(sld, (500,0), lowestrock):
        grains += 1
    print(f"part 1: {grains}")
    #print(f"part 2: {len(visitedk9)}")
 
print("Sample")
dec14("dec14s.txt")
#print("Actual")
#dec14("dec14.txt")