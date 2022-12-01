fname = "dec01.txt"

elfsums = []
grabelfsum = lambda l,s: l.append(sum([int(x) for x in s]))
with open(fname) as f:
    l = f.read().splitlines()
    while "" in l:
        elfend = l.index("") 
        elf = l[:elfend] # copy next elf's list
        l = l[elfend+1:] # shorten the master list
        grabelfsum(elfsums,elf) # sum each elf's list
    grabelfsum(elfsums,l) # sum the last elf's list
    print(f"max calorie elf is: {max(elfsums)}") # part 1
    print(f"top three total calories: {sum(sorted(elfsums)[-3:])}")
    