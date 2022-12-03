# Advent of code 03
from aocutils import *

# Sample:  157 and 70
# Actual:  7872 and 2497

def dec03(fname):
    lines = flistofstrings(fname)
    splits = [[x[:len(x)//2],x[len(x)//2:]] for x in lines]
    print(f"part 1: {sum([charpriority(list(set(x[0]).intersection(set(x[1])))[0]) for x in splits])}")
    triples = [[lines[3*x],lines[3*x+1],lines[3*x+2]] for x in range(len(lines)//3)]
    print(f"part 2: {sum([charpriority(list(set(x[0]).intersection(x[1]).intersection(x[2]))[0]) for x in triples])}")


print("Sample")
dec03("dec03s.txt")
print("Actual")
dec03("dec03.txt")