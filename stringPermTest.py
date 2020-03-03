

def getPermutations(s, startInd, strLength, allp=[]):
    # send back an array of all permutations of s

    if startInd == strLength:
        val = ''.join(s)
        allp.append(val)
    else:
        for j in range(startInd, strLength):
            s[startInd], s[j] = s[j], s[startInd]
            getPermutations(s, startInd+1, strLength)

    return allp

################################

def isPermutation(masterStr, compStr):
    # is compStr string a permutation of masteStr
    permFlag = 0

    allPermutations = getPermutations(list(compStr), 0, len(compStr))

    for ap in allPermutations:
        if ap == masterStr:
            permFlag = 1
            break

    return permFlag


################################

def printPermutationOrNot(ms, cs):
    print(cs + " is ", end="")
    if not isPermutation(ms, cs):
        print(" NOT ", end="") 
    print("a permutation of " + ms)

################################



strMaster = "CEB"
strTest = "ABC"

printPermutationOrNot(strMaster, strTest)

strMaster = "CAB"
strTest = "ABC"

printPermutationOrNot(strMaster, strTest)

