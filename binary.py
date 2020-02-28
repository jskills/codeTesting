
def addBinary(n1, n2):
	result = ''
	limit = 0
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
	while (i >= 0 ):
		sumVal, carry = addBinDigits(n1[i], n2[i], carry)
		result = str(sumVal) + result
		i -= 1
	if carry:
		result = "1" + result

	return result


def padArray(a, num):
	i = 1
	while i <= num:
		a = "0" + a
		i += 1
	return a


def addBinDigits(n1, n2, c):
	carry = 0
	retVal = 0
	sumDigits = int(n1) + int(n2) + int(c)
	if sumDigits == 3:
		retVal = 1
		carry = 1
	elif sumDigits == 2 :
		retVal = 0
		carry = 1
	else:
		retVal = sumDigits
		
	return retVal, carry

def convertBintoDecimal(b):
	count = len(str(b)) - 1
	d = 0
	i = count
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
 

		
