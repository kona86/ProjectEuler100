from functools import reduce


def multiplesof(a,b,to):
    # Mylsit is the list
    # result is the final value
    mylist,result = [] , None
    result = 0
    while to  != 0:
        to -= 1
        if ((to % a) == 0) :mylist.append(to)
        if ((to % b) ==0 ) : mylist.append(to)
    result = reduce(lambda a,b: a+b,mylist)
    return result
print(multiplesof(3,5,1000))
