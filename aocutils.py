from datetime import datetime

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
        

