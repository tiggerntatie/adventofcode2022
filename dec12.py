# Advent of code 12
from aocutils import *
from re import compile
# Sample:  31 and 
# Actual:   and 

def dec12(fname):
    [Monkey(*m, 1) for m in groupedstringlists(flistofstrings(fname))]
    for _ in range(20):
        for mid in range(len(Monkey.list)):
            m = Monkey.monkeyfromid(mid)
            m.turn()
    #print([m.inspectcount for m in Monkey.list.values()])
    top2 = sorted([m.inspectcount for m in Monkey.list.values()])[-2:]
    print(f"part 1: {top2[0]*top2[1]}")
    Monkey.clearmonkies()
    [Monkey(*m, 2) for m in groupedstringlists(flistofstrings(fname))]
    for _ in range(10000):
        for mid in range(len(Monkey.list)):
            m = Monkey.monkeyfromid(mid)
            m.turn()
    #print([m.inspectcount for m in Monkey.list.values()])
    top2 = sorted([m.inspectcount for m in Monkey.list.values()])[-2:]
    print(f"part 2: {top2[0]*top2[1]}")

print("Sample")
dec12("dec12s.txt")
#print("Actual")
#dec12("dec12.txt")
