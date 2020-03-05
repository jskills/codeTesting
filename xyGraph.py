import math
import random

def distanceFromOrigin(x, y, method='crow'):
    # if method is 'city', calculate hortizonal + vertical (city blocks)
    # if method is 'crow', calculate diagonal distance (as the crow flies)

    if method == 'crow':
        return math.sqrt(int(x)**2 + int(y)**2)
    elif method == 'city' :
        return abs(int(x)) + abs(int(y))
    else:
        print("Invalid method")
        return None
  


def returnLongestDistandCoordinates(aDict):
    longest = 0
    for a in aDict:
        if aDict[a] and aDict[a] > longest:
            longest = aDict[a]
            coordinates = a
    return longest, coordinates


def returnDistanceList(coordinateList, limit):
    # will return the list of coordinates closest to origin
    # limit is the number of coordinate pairs returned


    # initialize distance dictionary
    distanceDict = dict()

    i = 0
    while i < len(coordinateList):
        x,y = coordinateList[i].split(",")
        d = distanceFromOrigin(x,y)

        # if we have not satisifed the limit of coordinates we need to return yet
        # just add this pair to the dictionary
        # otherwise it can only be added if it is less than the longest distance in that dict

        if len(distanceDict) < limit:
            distanceDict[coordinateList[i]] = d
        else:
            longestDist, longestDistVal = returnLongestDistandCoordinates(distanceDict)
            if d < longestDist:
                # add this entry and boot the other with the longest distance
                distanceDict[coordinateList[i]] = d
                distanceDict[longestDistVal] = None
        i += 1

    returnList = list()
    # put coordinates into a list based on dictionary keys that have values
    for d in distanceDict:
        if distanceDict[d]:
            returnList.append(d)

    return returnList



##########################################

# generate a list of 100 points on a 2000 x 2000 grid
testList = list()
for i in range(1 , 100):
    x = random.randrange(-1000,1000,2)
    y = random.randrange(-1000,1000,2)
    testList.append(str(x) + ',' + str(y))


# return the k closest points
k = 5
returnL = returnDistanceList(testList, k)
print("Returning the " + str(k) + " closest coordinates to the origin")
for r in returnL:
    print(r)

