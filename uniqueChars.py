
def uniqueChars(inStr):
    # does this string have all unique characters?
    strIndex = 0
    uniqueFlag = 1
    compStr = inStr

    # initialize dictionary with zeros
    found = dict.fromkeys(inStr, 0)

    while (strIndex < len(inStr)):
        found[inStr[strIndex]] += 1
        
        if(found[inStr[strIndex]] > 1):
            uniqueFlag = 0
            break
        strIndex += 1
   
    return uniqueFlag 

################################

def printIsUnique(s):
    print s,
    if uniqueChars(s):
        print " has", 
    else:
        print " does not have",
    print " all unique characters"

################################

printIsUnique("jfjrosmvotonosopl")
printIsUnique('1234567890qwertyuio')
