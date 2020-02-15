#!/usr/bin/env python

import os
import sys
import re


def sortLists(*argv):

    # compute total number of elements in all passed in lists
    totalSizeNeeded = 0
    for listItem in argv:
        totalSizeNeeded += len(listItem)
    
    # allocate new array to sum of length all input lists
    bigList = [None] * totalSizeNeeded

    # insert all list values into single array
    count = 0
    for listItem in argv:
        for li in listItem:
            bigList[count] = li
            count += 1

    # sort the single array
    bigList.sort()
    
    # return results
    return bigList

#############################

a = [1, 5, 7]
b = [6, 9, 22]
c = [3, 5, 10, 2, 4]

outList = sortLists(a, b, c)

print outList









