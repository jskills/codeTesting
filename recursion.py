
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

def retStringPermutations(s, step=0, allP=[]):
    if step == len(s):
        # we've gotten to the end, add permutation to return list
        allP.append("".join(s))
    for i in range(step, len(s)):
        # copy the string (store as array)
        s_copy = list(s)
        # swap the current index with the step
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        # recurse on the portion of the string that has not been swapped yet
        retStringPermutations(s_copy, step + 1, allP)

    return allP


def isAnagram(s1, s2):
	s1Perms = retStringPermutations(s1)
	s2Perms = retStringPermutations(s2)
	for i1 in s1Perms:
		for i2 in s2Perms:
			if i1 == i2:
				return True
	return False

def isPalindrome(s):
	sList = list(s)
	cList = [''] * len(s)
	# get length minus 1 to use i as index through string converted to a list
	i = len(sList) - 1
	j = 0
	while i >= 0:
		cList[i] = sList[j]
		i -= 1
		j += 1

	return "".join(cList) == "".join(sList)


#############

#getStringPermutations('WOCK')
#allPs = retStringPermutations('WOCK')
#print(str(allPs))

v1 = 'RADAR'
v2 = 'ARRAD'
print (v1 + " and " + v2 + " anagrams: ", end="")
if isAnagram(v1, v2):
	print("Yup!")
else:
	print("Noope.")

print("Is " + v1 + " a palindrome : ", end="")
if isPalindrome(v1):
	print("Yes.")
else:
	print("Nah.")
print("Is " + v2 + " a palindrome :", end="")
if isPalindrome(v2):
        print("Yes.")
else:
        print("Nah.")
