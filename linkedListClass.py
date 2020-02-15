
class SLinkedList:
    def __init__(self):
        self.headNode = None

    class Node:
        def __init__(self, dataval=None):
            self.dataval = dataval
            self.nextNode = None

    def appendNode(self, val):
        top = self.headNode
        saveNode = top
        while top is not None:
            saveNode = top
            top = top.nextNode
        saveNode.nextNode = self.Node(val)

    def pruneDupes(self):
        checkDict = {}
        checkNode = self.headNode

        # precompute the linked list into a hash function of occurrences per value
        while checkNode is not None:
            if checkNode.dataval in checkDict:
                checkDict[checkNode.dataval] += 1
            else:
                checkDict[checkNode.dataval] = 1

            #print str(checkNode.dataval) + " has occurences " + str(checkDict[checkNode.dataval])
            checkNode = checkNode.nextNode


        # now use that list to identify dupes
        checkNode = self.headNode
        while checkNode is not None:
            # use hash lookup
            if checkDict[checkNode.dataval] > 1:
                # check for special case where the root node's value is in another node
                if checkNode == self.headNode:
                    # make the second node the root 
                    self.headNode = checkNode.nextNode
                else:
                    # check for case where any other node's value is in another node
                    # set previous node to point to next node, thus dropping current node into the ether
                    prevNode.nextNode = checkNode.nextNode
                # decrement the checkDict hash value since we removed a node
                checkDict[checkNode.dataval] -= 1
            else:
                # if we didn't delete a node, set the previous node value to the current node we just looked at
                prevNode = checkNode

            # then set checkNode to the next node in the list
            checkNode = checkNode.nextNode


    def findMiddleNode(self, headNode):
        # set both iterators to root node
        oneATAT = twoATAT = headNode
        # move through the list - one iterator one node at a time, the other two at a time
        # the slower iterator ends up in the middle
        while twoATAT.nextNode is not None and twoATAT.nextNode.nextNode is not None:
            oneATAT = oneATAT.nextNode
            twoATAT = twoATAT.nextNode.nextNode
        return oneATAT
    
    def mergeSort(self, headNode):
        if headNode is None or headNode.nextNode is None:
            return headNode

        midNode = self.findMiddleNode(headNode)
        next2midNode = midNode.nextNode
        # cut list in half
        midNode.nextNode = None
        
        # recursively call this method on both left and right sides until sorted
        left = self.mergeSort(headNode)
        right = self.mergeSort(next2midNode)

        # merge left and right together
        sortedList = self.merge(left, right)

        return sortedList


    def merge(self, a, b):
        result = None

        # best cases
        if a == None:
            return b
        if b == None:
            return a

        if a.dataval <= b.dataval:
            result = a
            result.nextNode = self.merge(a.nextNode, b)
        else:
            result = b
            result.nextNode = self.merge(a, b.nextNode)

        return result
        
        

    def listprint(self):
        printval = self.headNode
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextNode


#######################

