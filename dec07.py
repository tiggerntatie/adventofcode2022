# Advent of code 07
from aocutils import *
from re import compile
# Sample:  95437 and 1334506
# Actual:    and 


def getdirsize(root, runningtot, spacerequired):
    total = 0
    # gather directories
    for v in root[3].values():
        total += getdirsize(v, runningtot, spacerequired)
    # gather files
    for v in root[2].values():
        total += v
    if total <= 100000:
        runningtot[0] += total 
    if spacerequired and total >= spacerequired and total < runningtot[1]:
        runningtot[1] = total
    return total

def dec07(fname):
    tree = {}
    cdir = None
    scd = compile("\$ cd (.+)")
    sls = compile("\$ ls")
    sditem = compile("(dir|\d+) (.+)")

    for l in flistofstrings(fname):
        if m := scd.search(l):
            newdir = m.group(1)
            if newdir == '/':
                cdir = tree.setdefault('/', [None, '/', {}, {}])  # establish root directory, no parent, named /, no files, no subdirs
            elif newdir == '..':
                cdir = cdir[0]  # step up one level
            else:               # step down one level
                cdir = cdir[3][newdir]
        elif m := sls.search(l):
            pass  # just commanding a directory list
        else:
            m = sditem.search(l)
            if m.group(1) == 'dir':
                cdir[3].setdefault(m.group(2), [cdir, m.group(2), {}, {}])  # establish a directory
            else:
                cdir[2][m.group(2)] = int(m.group(1))   # establish a file with size

    atmost100k = [0,100000000]  # running total of directories <= 100000, smallest directory >= 30000000
    rootsize = getdirsize(tree['/'], atmost100k, None)
    getdirsize(tree['/'], atmost100k, 30000000 - (70000000-rootsize))  # computed free space required

    print(f"part 1: {atmost100k[0]}")
    print(f"part 2: {atmost100k[1]}")
 
print("Sample")
dec07("dec07s.txt")
print("Actual")
dec07("dec07.txt")