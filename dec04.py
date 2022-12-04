# Advent of code 04
from aocutils import *

# Sample:  2 and 518
# Actual:  4 and 909

def dec04(fname):
    lines = flistofstrings(fname)
    pairs = [[[int(z) for z in y.split('-')] for y in x] for x in 
                [x.split(',') for x in lines]]
    print(f"part 1: {sum([rangecontainsrange(*a[0],*a[1]) for a in pairs])}")
    print(f"part 2: {sum([rangeoverlapsrange(*a[0],*a[1]) for a in pairs])}")

print("Sample")
dec04("dec04s.txt")
print("Actual")
dec04("dec04.txt")