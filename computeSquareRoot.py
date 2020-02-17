
def squareRoot(val):
    # add all odd numbers starting at 1 until the sum is greater than the passed in value
    # the number of odd numbers is the square root

    i = cnt = rollingSum = 1
    while rollingSum < val:
        i += 2
        rollingSum += i
        cnt += 1
  
    perfect = False
    if rollingSum == val:
        perfect = True 
    else:
        # return floor value
        cnt -= 1

    return cnt, perfect

#####################################

passVal = 1
while passVal < 100:
    sqrt, status = squareRoot(passVal)
    print "The Square Root of " + str(passVal),
    if status == True:
        print "is exactly ",
    else:
        print "has a floor() of ",
    print str(sqrt)
    passVal += 1
    
