# flistofstrings
# convert text file into a list of strings
def flistofstrings(fname):
    with open(fname) as f:
        return f.read().splitlines()

# flistofintegers
# convert text file of integers into a list of integers
def flistofintegers(fname):
    with open(fname) as f:
        return [int(x) for x in flistofstrings(fname)]

# groupedstringlists
# convert list of grouped strings into list of string lists
#
# a
# b
# 
# c
# 
# becomes [['a','b'],['c']]
# 
def groupedstringlists(listin):
    if not "" in listin:
        return [listin]
    boundary = listin.index("")
    return [listin[:boundary]] + groupedstringlists(listin[boundary+1:])

# groupedintlists
# convert list of grouped integer strings to integers
def groupedintlists(groupedstringlist):
    ret = []
    for l in groupedstringlist:
        ilist = [int(x) for x in l]
        ret.append(ilist)
    return ret
        
# charpriority
# convert character to integer: a = 1, A = 27, b = 2, etc..
charpriority = lambda c: ord(c)-ord('A')+27 if c.isupper() else ord(c)-ord('a')+1

# rangecontainsrange
# does range of one value set lie entirely within another
def rangecontainsrange(astart, aend, bstart, bend):
    ainb = lambda ast, ae, bs, be: ast >= bs and ae <= be
    return ainb(astart, aend, bstart, bend) or ainb(bstart, bend, astart, aend)

#rangeoverlapsrange
# does range of one value set overlap at all with another
def rangeoverlapsrange(astart, aend, bstart, bend):
    aoverb = lambda ast, ae, bs, be: ast >= bs and ast <= be
    return (rangecontainsrange(astart, aend, bstart, bend) or 
            aoverb(astart, aend, bstart, bend) or
            aoverb(bstart, bend, astart, aend))