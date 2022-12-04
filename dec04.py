# Advent of code 04
from aocutils import *
from re import findall

# Sample:  2 and 518
# Actual:  4 and 909

def dec04(fname):
    s = "(\d+)-(\d+),(\d+)-(\d+)"
    data = [[int(y) for y in findall(s,x)[0]] for x in flistofstrings(fname)]
    print(f"part 1: {sum([rangecontainsrange(*a) for a in data])}")
    print(f"part 2: {sum([rangeoverlapsrange(*a) for a in data])}")

print("Sample")
dec04("dec04s.txt")
print("Actual")
dec04("dec04.txt")