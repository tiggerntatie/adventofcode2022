# Advent of code 16
from re import compile
from collections import Counter
from aocutils import *
# Sample: and 
# Actual: and 

     

def dec16(fname):
    ins = compile(".*=([\d\-]+).*=([\d\-]+).*=([\d\-]+).*=([\d\-]+)")
    ml = [[int(m.group(i)) for i in range(1,5)] for m in [ins.search(s) for s in flistofstrings(fname)]]
    ml = [l + [mdist(*l)] for l in ml]
    print(f"part 1: {count}")

    #print(f"part 2: {tfreq}")


print("Sample")
dec16("dec16s.txt")
print("Actual")
dec16("dec16.txt")  
