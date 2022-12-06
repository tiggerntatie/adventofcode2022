# Advent of code 06
from aocutils import *

# Sample:  11 and 26
# Actual:   1804 and 2508

def gatherresult(x):
    result = ""
    for c in x:
        if c:
            result += c[0]
    return result

def dec06(fname):
    lines = flistofstrings(fname) # only one line!
    pktwindow = list("_"*4)
    msgwindow = list("_"*14)
    part1done = False
    for n, c in enumerate(lines[0]):
        pktwindow.pop(0)
        pktwindow.append(c)
        msgwindow.pop(0)
        msgwindow.append(c)
        if n > 2:
            if not part1done and len(set(pktwindow)) == 4:
                print(f"part 1: {n+1}")
                part1done = True
            if len(set(msgwindow)) == 14:
                print(f"part 2: {n+1}")
                break

print("Sample")
dec06("dec06s.txt")
print("Actual")
dec06("dec06.txt")