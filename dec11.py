# Advent of code 11
from aocutils import *
from re import compile
# Sample:  10605 and 2713310158
# Actual:  112815 and 25738411485

class Monkey():
    list = {}
    mod = 1
    def __init__(self, mname, items, op, test, t, f, stage):
        opregex = compile(".*Operation: new = (old|[\d]+) ([\*\+]) (old|[\d]+)")
        self.id = int(mname[-2:-1])
        self.items = [int(n) for n in (items[18:].split(','))]
        _ = opregex.search(op)
        self.op = [_.group(1) if _.group(1) == 'old' else int(_.group(1)), 
                    _.group(2),
                    _.group(3) if _.group(3) == 'old' else int(_.group(3))]
        self.test = int(test[21:])
        Monkey.mod *= self.test   # for part 2
        self.t = int(t[-1:])
        self.f = int(f[-1:])
        Monkey.list[self.id] = self
        self.inspectcount = 0
        self.stage = stage
        self.debug = False
        
    @classmethod
    def monkeyfromid(cls, id):
        return cls.list[id]
    
    @classmethod
    def clearmonkies(cls):
        cls.list = {}
        cls.mod = 1

    def __str__(self):
        return f"Monkey {self.id}, {self.items}, {self.op}, {self.test}, {self.t}, {self.f}"

    def log(self, s):
        if self.debug:
            print(s)

    def turn(self):
        self.log(f"Monkey {self.id}:")
        for w in self.items:
            self.log(f"  Monkey inspects an item with a worry level of {w}.")
            self.inspectcount += 1
            a = w if self.op[0] == 'old' else self.op[0]
            b = w if self.op[2] == 'old' else self.op[2]
            o = self.op[1]
            if o == '*':
                w = a * b
            else:
                w = a + b
            self.log(f"    Worry level is {a}{o}{b} and changes to {w}.")
            if self.stage == 1:
                w //= 3 # default transform
            self.log(f"    Monkey gets bored with item. Worry level is divided by 3 to {w}")
            if not w % self.test:
                self.log(f"    Current worry level is not divisible by {self.test}")
                dest = self.t
            else:
                dest = self.f
            if self.stage == 2:
                w = w % self.mod
            self.monkeyfromid(dest).throw(w)
            self.log(f"    Item with worry level {w} is thrown to monkey {dest}")
        self.items = []

    def throw(self, w):
        self.items.append(w)
    
def dec11(fname):
    [Monkey(*m, 1) for m in groupedstringlists(flistofstrings(fname))]
    for _ in range(20):
        for mid in range(len(Monkey.list)):
            m = Monkey.monkeyfromid(mid)
            m.turn()
    #print([m.inspectcount for m in Monkey.list.values()])
    top2 = sorted([m.inspectcount for m in Monkey.list.values()])[-2:]
    print(f"part 1: {top2[0]*top2[1]}")
    Monkey.clearmonkies()
    [Monkey(*m, 2) for m in groupedstringlists(flistofstrings(fname))]
    for _ in range(10000):
        for mid in range(len(Monkey.list)):
            m = Monkey.monkeyfromid(mid)
            m.turn()
    #print([m.inspectcount for m in Monkey.list.values()])
    top2 = sorted([m.inspectcount for m in Monkey.list.values()])[-2:]
    print(f"part 2: {top2[0]*top2[1]}")

print("Sample")
dec11("dec11s.txt")
print("Actual")
dec11("dec11.txt")