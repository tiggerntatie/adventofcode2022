# Advent of code 01
from aocutils import *

# sample: 24000 and 45000
# actual: 70374 and 204610
    
def dec01(fname):
    groups = groupedstringlists(flistofstrings(fname))
    igroups = groupedintlists(groups)
    sums = [sum(x) for x in igroups]
    print(f"part 1: {max(sums)}")
    print(f"part 2: {sum(sorted(sums)[-3:])}")

print("Sample")
dec01("dec01s.txt")
print("Actual")
dec01("dec01.txt")