

def getPermutations(s, startInd, strLength):
    # send back an array of all permutations of s

    if startInd == strLength:
        val = ''.join(s)
        print val
        return val
    else:
        for j in range(startInd, strLength):
            s[startInd], s[j] = s[j], s[startInd]
            getPermutations(s, startInd+1, strLength)
            s[startInd], s[j] = s[j], s[startInd]


################################

def isPermutation(masterStr, compStr):
    # is compStr string a permutation of masteStr
    permFlag = 0

    allPermutations = []
    getPermutations(list(compStr), 0, len(compStr))

    for ap in allPermutations:
        print "ap = " + ap
        if ap == masterStr:
            permFlag = 1
            break

    return permFlag


################################

def printPermutationOrNot(ms, cs):
    print cs + " is",
    if not isPermutation(ms, cs):
        print " NOT ", 
    print "a permutation of " + ms

################################



strMaster = "CAB"
strTest = "ABC"

printPermutationOrNot(strMaster, strTest)

