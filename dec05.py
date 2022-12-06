# Advent of code 05 7:25-
from aocutils import *
from re import findall

# Sample:  CMZ and MCD
# Actual:  GRTSWNJHH and QLFQDBBHM

def gatherresult(x):
    result = ""
    for c in x:
        if c:
            result += c[0]
    return result

def dec05(fname):
    cols = [[],[],[],[],[],[],[],[],[]]
    s = "move (\d+) from (\d+) to (\d+)"
    lines = flistofstrings(fname)
    i = 0
    while lines[i][1] != '1':   # gather the stacks
        j = 0
        while j*4 < len(lines[i]):
            col = lines[i][1+j*4]
            if col != ' ':
                cols[j].append(col)
            j += 1
        i += 1
    cols2 = cols[::]                    # another copy for part 2
    for step in lines[i+2:]:            # gather the moves and execute them
        (n, f, t) = (int(x) for x in findall(s, step)[0])
        temp = cols[f-1][:n]
        temp2 = cols2[f-1][:n]
        cols[f-1] = cols[f-1][n:]       # from..
        cols2[f-1] = cols2[f-1][n:]
        cols[t-1] = temp[::-1] + cols[t-1]    # to
        cols2[t-1] = temp2 + cols2[t-1]
    
    print(f"part 1: {gatherresult(cols)}")
    print(f"part 2: {gatherresult(cols2)}")
    
print("Sample")
dec05("dec05s.txt")
print("Actual")
dec05("dec05.txt")