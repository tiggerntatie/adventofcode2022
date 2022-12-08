# Advent of code 08
from aocutils import *
from re import compile
# Sample:  21 and 8
# Actual:  1708 and 504000

# check visibility in one direction
def isvisible(n, s):
    if not n:                       # n is at the start of the string
        return True
    if ord(s[0]) >= ord(s[n]):      # start of the string is bigger
        return False
    return isvisible(n-1, s[1:])    # solve a slightly smaller case

# check number of visible trees in one direction
def visibletrees(n, s):
    if not n:                       # n is at the start of the string
        return 0
    if ord(s[n-1]) >= ord(s[n]):    # right next to same or higher 
        return 1
    return 1 + visibletrees(n-1, s[:n-1]+s[n:]) # recurse, and so on...

def dec08(fname):
    rows = flistofstrings(fname)
    width = len(rows[0])
    height = len(rows)
    # build a list of orthogonal strings
    columns = ["".join([r[n] for r in rows]) for n in range(height)]
    vcount = 0              # initialize visibles
    vismax = 0          
    for c in range(width):
        for r in range(height):
            if (isvisible(r, columns[c]) or 
                isvisible(height-r-1, columns[c][::-1]) or
                isvisible(c, rows[r]) or
                isvisible(width-c-1, rows[r][::-1])
            ):
                vcount += 1
            vtrees = (visibletrees(r, columns[c]) * 
                visibletrees(height-r-1, columns[c][::-1]) *
                visibletrees(c, rows[r]) *
                visibletrees(width-c-1, rows[r][::-1]))
            if vtrees > vismax:
                vismax = vtrees

    print(f"part 1: {vcount}")
    print(f"part 2: {vismax}")
 
print("Sample")
dec08("dec08s.txt")
print("Actual")
dec08("dec08.txt")