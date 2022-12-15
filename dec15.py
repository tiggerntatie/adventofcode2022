# Advent of code 15
from re import compile
from aocutils import *
# Sample: row 10: 26  and 
# Actual: row 2000000:  and  

def mdist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

# start and end x-coordinates for y-row positions less than distance to x,y
def boundsdist(yrow, dist, x, y):
    deltax = dist-abs(y-yrow)-1
    if deltax < 0:
        return False # nothing on this row is excluded
    return (x-deltax, x+deltax)

# take a list of spans, find overlaps, and return a new list
# spans are in the form [lo, hi]. Identical lo and hi indicate single place span
# hi > lo is an invalid span and is dropped
def spanjoiner(spans):
    def aoverlapb(a1, a2, b1, b2):
        if a1 >= b1 and a2 <= b2: # a inside b
            return [b1, b2]
        if b1 >= a1 and b2 <= a2: # b inside a
            return [a1, b2]
        if a1 < b1 and a2 <= b2: # a then overlap b
            return [a1, b2]
        if b1 < a1 and b2 <= a2: # b then overlap a
            return [b1, a2]
        return False
    # does first overlap anything else?
    print(spans)
    if len(spans) <= 1:
        return spans
    first = spans[0]
    rest = spans[1:]
    matches = []
    for s in rest:
        if ol := aoverlapb(*first, *s):
            # found a match
            print(f"ol: {}")
            first = ol
            matches.append(s)
    # update rest without matched spans
    print(f"rest1 {rest}")
    print(f"matches {matches}")
    rest = list(filter(lambda s: s not in matches, rest))
    print(f"rest2 {rest}")
    joined = spanjoiner(rest)
    return first + spanjoiner(rest)
  

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


def excludedcount(ml, row):
    ranges = [boundsdist(row, l[4], l[0], l[1]) for l in ml]
    # remove null ranges
    ranges = list(filter(lambda x: x[0] != x[1], ranges))
    return 0
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
    # ml is now list of 5: sensorxy, beaconxy, distance
    spans = spanjoiner(list(filter(lambda x: x, [boundsdist(row, l[4], l[0], l[1]) for l in ml])))
    rowbeacons = sum([l[3] == row for l in ml])
    count = sum([l[1]-l[0]+1 for l in spans]) - rowbeacons

    print(f"part 1: {count}")
    #print(f"part 2: {count}")
 
 


print("Sample")
dec15("dec15s.txt", 10)
#print("Actual")
#dec15("dec15.txt", 2000000)
