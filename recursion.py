
def getStringPermutations(s, step=0):
    if step == len(s):
        # we've gotten to the end, print the permutation
        print("".join(s)) 
    for i in range(step, len(s)):
        # copy the string (store as array)
        s_copy = list(s)
        # swap the current index with the step
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        # recurse on the portion of the string that has not been swapped yet
        getStringPermutations(s_copy, step + 1)

def retStringPermutations(s, step=0, allP=list()):
    if step == len(s):
        # we've gotten to the end, add permutation to return list
        print("".join(s))
        allP.append("".join(s))
    for i in range(step, len(s)):
        # copy the string (store as array)
        s_copy = list(s)
        # swap the current index with the step
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        # recurse on the portion of the string that has not been swapped yet
        retStringPermutations(s_copy, step + 1, allP)

        return allP


def isPalindrome(s1, s2):
    if foo:
        bar = 1

#############

#getStringPermutations('WOCK')
print(retStringPermutations('WOCK'))

