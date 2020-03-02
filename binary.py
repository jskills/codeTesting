
def addBinary(n1, n2):
	# parsing two strings that represent binary numbers and adding them
	result = ''
	limit = 0
	# compute the length of both strings
	# if the two strings are not the same length, pad the shorter one with leading zeros
	if len(n1) > len(n2):
		limit = len(n1)
		n2 = padArray(n2, len(n1) - len(n2))
	elif len(n1) < len(n2):	
		n1 = padArray(n1, len(n2) - len(n1))
		limit = len(n2)
	else:
		limit = len(n1)
	i = limit - 1
	sumVal = carry = 0
	print(n1)
	print(n2)
	# addressing each string's array values
	# iterate over each digit of the strings for each 
	while (i >= 0 ):
		# pass each digit value to the addBinDigits method
		# along with the carry flag
		# that method returns the result of adding two binary digits and whether to carry 1 or not
		sumVal, carry = addBinDigits(n1[i], n2[i], carry)
		# concatente the return value in front of the result string
		result = str(sumVal) + result
		i -= 1
	if carry:
		# if the carry value is 1, add a "1" to the left of the result string
		result = "1" + result

	# return the final result string
	return result


def padArray(a, num):
	i = 1
	while i <= num:
		a = "0" + a
		i += 1
	return a


def addBinDigits(n1, n2, c):
	# this method adds two binary digits considering the carry value
	carry = 0
	retVal = 0
	sumDigits = int(n1) + int(n2) + int(c)
	# add the digits and the carry val and decide what to send back
	# if carry is 1 and both params are 1, we send back 1 and carry 1
	# if any of the 3 add up to 2 we return 0 and send back carry 1
	# otherwise we just send back the sum of the digits (1 or 0)
	if sumDigits == 3:
		retVal = 1
		carry = 1
	elif sumDigits == 2 :
		retVal = 0
		carry = 1
	else:
		retVal = sumDigits
	
	# return both the value of the addition as well as the carry flag	
	return retVal, carry

def convertBintoDecimal(b):
	count = len(str(b)) - 1
	d = 0
	i = count
	# iterate over the binary string digit by digit
	# start the index at the length of the string - 1 and countinue to zero
	# to parse from right to left
	# inside the loop, add 2 to the power of the current index of the string array
	while i > -1:
		if int(b[i]):
			d += 2**(count - i)
		i -= 1
	return d


######################################################

n1 = '10101010'
n2 = '11001100'

bSum = addBinary(n1, n2)

print('Adding binary values : ' + n1 + ' and ' + n2 + ' = ' + bSum)

print('Converting binary ' + bSum + ' to decimal ' + str(convertBintoDecimal(bSum)))
 
