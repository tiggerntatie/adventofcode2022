# Advent of code 13
from functools import cmp_to_key
from aocutils import *
# Sample:  13 and 5825
# Actual:  140 and 24477

# items must be lists
def isrightorderlists(left, right):
    if not len(left) and not len(right):
        return None        
    elif not len(left) and len(right):
        return True
    elif len(left) and not len(right):
        return False
    else:
        for i in range(max(len(left), len(right))):
            if i == len(left):
                return True     # ran out of items on left
            elif i == len(right):
                return False    # ran out of items on the right
            elif type(left[i]) is list and type(right[i]) is list:
                temp = isrightorderlists(left[i], right[i])
                if temp:
                    return True
                elif temp == False:
                    return False
                # otherwise, must be None, so keep going
            elif type(left[i]) is int and type(right[i]) is int:
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
            elif type(left[i]) is int and type(right[i]) is list:
                temp = isrightorderlists([left[i]], right[i])
                if temp:
                    return True
                elif temp == False:
                    return False
                # otherwise, must be None, so keep going
            elif type(left[i]) is list and type(right[i]) is int:
                temp = isrightorderlists(left[i], [right[i]])
                if temp:
                    return True
                elif temp == False:
                    return False

    
def keywrapper(left, right):
    temp = isrightorderlists(left, right)
    if temp == False:
        return 1
    if temp == None:
        return 0
    if temp == True:
        return -1



def dec13(fname):
    newd = []
    data = groupedstringlists(flistofstrings(fname))
    for pair in data:
        for item in pair:
            newd.append(eval(item))
    correctpairs = []
    for i in range(0,len(newd),2):
        if isrightorderlists(newd[i], newd[i+1]):
            correctpairs.append((i//2)+1)
    print(f"part 1: {sum(correctpairs)}")
    # now add a couple and attempt a sort
    newd.append([[2]])
    newd.append([[6]])
    newd.sort(key=cmp_to_key(keywrapper))
    print(f"part 2: {(newd.index([[2]])+1)*(newd.index([[6]])+1)}")
 
print("Sample")
dec13("dec13s.txt")
print("Actual")
dec13("dec13.txt")