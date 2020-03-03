import time
import sys
sys.setrecursionlimit(5000)

def printFib(limit, useHash=0, map=dict()):
    # print the limit nmber in the Fibonacci sequence

    if limit == 0:
        return 0 
    elif limit == 1:
        return 1
    elif limit in map and useHash:
        return map[limit] 
    else:
        # since we are running this method twice
        # AND we will be repeating values
        # it's more efficient to use a hash mapping to store previous results
        # as to avoid unnecessarily recomputing values we already have from this method
        tmp_val = printFib(limit-1, useHash, map) + printFib(limit-2, useHash, map)
        if useHash:
            map[limit] = tmp_val
        return tmp_val

def printFibSequence(limit, useHash):
    # print the entire list up to limit
    i = 0
    while i <= limit:
        print("item # " + str(i))
        print(str(printFib(i, useHash)))
        i += 1

######################

limit =  35

start_time = time.time()
#printFibSequence(limit, 0)
print(str(printFib(limit, 0)))
end_time = time.time()
runTime = end_time - start_time
print("Run time 1 in seconds : " + str(round(runTime,4)))

limit = 1000

start_time2 = time.time()
#printFibSequence(limit, 1)
print(str(printFib(limit, 1)))
end_time2 = time.time()
runTime2 = end_time2 - start_time2
print("Run time 2 in seconds : " + str(round(runTime2,4)))

