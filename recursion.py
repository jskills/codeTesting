
def getStringPermutations(s, step=0):
    if step == len(s):
        # we've gotten to the end, print the permutation
        print("".join(s)) 
    for i in range(step, len(s)):
        # copy the string (store as array)
        s_copy = [c for c in s]
        # swap the current index with the step
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        # recurse on the portion of the stringthat has not been swapped yet
        getStringPermutations(s_copy, step + 1)

#############

print(getStringPermutations('WOCK'))

