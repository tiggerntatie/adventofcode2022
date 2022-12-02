# Advent of code 02
from aocutils import *

# Sample: 15 and 12
# Actual: 13924 and 13448

LDW = [0, 3, 6]
values = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3,}
rules = {'X':{'A':'Z', 'B':'X', 'C':'Y'}, 
        'Y':{'A':'X', 'B':'Y', 'C':'Z'}, 
        'Z':{'A':'Y', 'B':'Z', 'C':'X'}, }
winvalues = {'X':0, 'Y':3, 'Z':6}

def game1(them, me):
    vt = values[them]
    vm = values[me]
    mescore = values[me]
    if vt == vm:
        return 3 + mescore
    if vm - vt == 1 or vt - vm == 2:
        return 6 + mescore
    return mescore

def game2(them, me):
    return values[rules[me][them]] + winvalues[me]

def dec02(fname):
    pairs = [x.split() for x in flistofstrings(fname)]
    print(f"part 1: {sum([game1(*x) for x in pairs])}") 
    print(f"part 2: {sum([game2(*x) for x in pairs])}")

print("Sample")
dec02("dec02s.txt")
print("Actual")
dec02("dec02.txt")