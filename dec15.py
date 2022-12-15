# Advent of code 15
from re import compile
from aocutils import *
# Sample: row 10: 26  and 
# Actual: row 2000000:  and  

def mdist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

# start and end x-coordinates for y-row positions less or equal to distance to x,y
def boundsdist(yrow, dist, x, y):
    deltax = dist-abs(y-yrow)+1
    if deltax < 0:
        return False # nothing on this row is excluded
    return [x-deltax, x+deltax]

# take a list of spans, find overlaps, and return a new list
# spans are in the form [lo, hi]. Identical lo and hi indicate single place span
# hi < lo is an invalid span 
def oldspanjoiner(spans):
    def aoverlapb(a1, a2, b1, b2):
        if a1 >= b1 and a2 <= b2: # a inside b
            return [b1, b2]
        if b1 >= a1 and b2 <= a2: # b inside a
            return [a1, a2]
        if a1 < b1 and a2 >= b1 and a2 <= b2: # a then overlap b
            return [a1, b2]
        if b1 < a1 and b2 >= a1 and b2 <= a2: # b then overlap a
            return [b1, a2]
        return False
        
    print(f"spans in: {spans}")    
    # does first overlap anything else?
    if len(spans) <= 1:
        return spans
    first = spans[0]
    rest = spans[1:]
    matches = []
    for s in rest:
        print(f"checking {first} and {s}")
        if ol := aoverlapb(*first, *s):
            print("matched!")
            # found a match
            first = ol
            matches.append(s)
    # update rest without matched spans
    rest = list(filter(lambda s: s not in matches, rest))
    print(f"first: {first}")
    joined = spanjoiner(rest)
    print(f"spans out: {[first]+joined}")    
    return [first] + joined

# take a list of spans, find overlaps, and return a new list
# spans are in the form [lo, hi]. Identical lo and hi indicate single place span
# hi < lo is an invalid span 
def spanjoiner(spans):
    # overlap and combine - assumes (b1,b2) >= (a1,a2)
    def aoverlapb(a1, a2, b1, b2):
        if a1 == b1 and a2 == b2:
            return [a1, a2]
        if b2 <= a2:
            return [a1, a2]  # b inside a
        if b2 > a2 and b1 <= a2:
            return [a1, b2]  # a overlaps b
        return False
        
    ospans = sorted(spans)    
    changed = True
    while changed:
        newspans = []
        i = 0
        changed = False
        while i < len(ospans) - 1:
            if ol := aoverlapb(*ospans[i], *ospans[i+1]):
                newspans.append(ol)
                changed = True
                i += 2
            else:
                newspans.append(ospans[i])
                i += 1
        ospans = newspans
    return ospans        

def dec15(fname, row):
    ins = compile(".*=([\d\-]+).*=([\d\-]+).*=([\d\-]+).*=([\d\-]+)")
    ml = [[int(m.group(i)) for i in range(1,5)] for m in [ins.search(s) for s in flistofstrings(fname)]]
    ml = [l + [mdist(*l)] for l in ml]
    # ml is now list of 5: sensorxy, beaconxy, distance
    spans = spanjoiner(list(filter(lambda x: x, [boundsdist(row, l[4], l[0], l[1]) for l in ml])))
    rowbeacons = list(filter(lambda l: l[3] == row, ml))
    rowbeacons = set([(l[2],l[3]) for l in rowbeacons])
    # onlyl count rowbeacons within spans
    print(f"spans {spans}")
    print(f"rowbeacons {rowbeacons}")
    rbc = 0
    for s in spans:
        for b in rowbeacons:
            if b[0] >= s[0] and b[0] <= s[1]:
                rbc += 1
    count = sum([l[1]-l[0]+1 for l in spans]) - rbc

    print(f"part 1: {count}")
    #print(f"part 2: {count}")


print("Sample")
dec15("dec15s.txt", 10)
print("Actual")
dec15("dec15.txt", 2000000)  # 4729524 is not correct!!
