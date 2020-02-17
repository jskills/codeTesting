
def printFib(limit):
    # print the limit nmber in the Fibonacci sequence

    if limit == 0:
        return 0 
    elif limit == 1:
        return 1 
    else:
        return printFib(limit-1) + printFib(limit-2)

def printFibSequence(limit):
    # print the entire list up to limit
    i = 0
    while i <= limit:
        print "item # " + str(i)
        print str(printFib(i))
        i += 1

######################

limit = 6 
printFibSequence(limit)
