# Advent of code 15
from re import compile
from aocutils import *
# Sample: row 10: 26  and 
# Actual: row 2000000:  and  

def mdist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

# start and end x-coordinates for y-row positions less than distance to x,y
def boundsdist(yrow, dist, x, y):
    deltax = dist-abs(y-yrow)
    if deltax <= 0:
        return (0,0) # nothing on this row is excluded
    return (x-deltax+1, x+deltax-1)

def excludedcount(ml, row):
    #ranges = [boundsdist(row, )]
    pass

def dec15(fname):
    ins = compile(".*=([\d\-]+).*=([\d\-]+).*=([\d\-]+).*=([\d\-]+)")
    ml = [[int(m.group(i)) for i in range(1,5)] for m in [ins.search(s) for s in flistofstrings(fname)]]
    ml = [x.extend(mdist(*x)) for x in ml]
    print(ml)
    #print(f"part 1: {grains}")
    #print(f"part 2: {grains}")
 
print("Sample")
dec15("dec15s.txt")
#print("Actual")
#dec15("dec15.txt")
