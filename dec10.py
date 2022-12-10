# Advent of code 10
from aocutils import *
# Sample:  13140 and 
# Actual:  12540 and FECZELHE

def paintscreen(disp, c, x):
    dchar = '.'
    xpos = (x) % 40
    cpos = (c-1) % 40
    if  x >= 0 and cpos > xpos-2 and cpos < xpos+2:
        dchar = '#'
    index = (c-1)//40
    disp[index] = disp[index]+dchar

def dec10(fname):
    instrs = []
    display = ["","","","","",""]
    strength = 0
    testcycle = lambda c: c in [20, 60, 100, 140, 180, 220]
    for l in flistofstrings(fname):
        if l[:4] == "addx":
            instrs.append(('addx', int(l[4:])))
        else:
            instrs.append(('noop',))
    x = 1
    c = 1
    for i in instrs:
        if i[0] == 'noop':
            if testcycle(c):
                strength += x*c
            paintscreen(display, c, x)
            c += 1
        else:
            if testcycle(c):
                strength += x*c
            paintscreen(display, c, x)
            c += 1
            if testcycle(c):
                strength += x*c
            paintscreen(display, c, x)
            c += 1
            x += i[1]

    print(f"part 1: {strength}")
    print(f"part 2:")
    for l in display:
        print(l)

print("Sample")
dec10("dec10s.txt")
print("Actual")
dec10("dec10.txt")