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
    return (x-deltax, x+deltax)

def oldexcludedcount(ml, row):
    ranges = [boundsdist(row, l[4], l[0], l[1]) for l in ml]
    exc = set()
    for r in ranges:
        print(r)
        if r[0] != r[1]:
            exc.update(range(r[0], r[1]+1))
    # remove known beacons
    for l in ml:
        if l[3] == row and l[2] in exc:
            exc.remove(l[2])
    return len(exc)

def aoverlapb(a1, a2, b1, b2):
    if a1 >= b1 and a2 <= b2: # a inside b
        return (b1, b2)
    if b1 >= a1 and b2 <= a2: # b inside a
        return (a1, b2)
    if a1 < b1 and a2 <= b2: # a then overlap b
        return (a1, b2)
    if b1 < a1 and b2 <= a2: # b then overlap a
        return (b1, a2)
    return False

def excludedcount(ml, row):
    ranges = [boundsdist(row, l[4], l[0], l[1]) for l in ml]
    # remove null ranges
    ranges = list(filter(lambda x: x[0] != x[1], ranges))
    done = False
    while not done:
        restart = False
        for i in range(len(ranges)-1):
            for j in range(1, len(ranges)):
                if crange := aoverlapb(*ranges[i], *ranges[j]):
                    ranges[i] = crange
                    del(ranges[j])
                    restart = True
                    break
                elif i == len(ranges)-2 and j == len(ranges)-1:
                    done = True
            if restart:
                break
    count = 0
    for r in ranges:
        count += r[1]-r[0]
        for l in ml:    # remove any beacons in this range
            if l[3] == row and l[2] >= r[0] and l[2] <= r[1]:
                count -= 1
    return count


def dec15(fname, row):
    ins = compile(".*=([\d\-]+).*=([\d\-]+).*=([\d\-]+).*=([\d\-]+)")
    ml = [[int(m.group(i)) for i in range(1,5)] for m in [ins.search(s) for s in flistofstrings(fname)]]
    ml = [l + [mdist(*l)] for l in ml]
    count = excludedcount(ml, row)
    print(f"part 1: {count}")
    #print(f"part 2: {count}")
 
print("Sample")
dec15("dec15s.txt", 10)
print("Actual")
#dec15("dec15.txt", 2000000)
