
class SLinkedList:
    def __init__(self):
        self.headval = None

    class Node:
        def __init__(self, dataval=None):
            self.dataval = dataval
            self.nextval = None

    def appendNode(self, val):
        top = self.headval
        saveNode = top
        while top is not None:
            saveNode = top
            top = top.nextval
        saveNode.nextval = self.Node(val)

    def pruneDupes(self):
        checkDict = {}
        checkNode = self.headval

        # precompute the linked list into a hash function of occurrences per value
        while checkNode is not None:
            if checkNode.dataval in checkDict:
                checkDict[checkNode.dataval] += 1
            else:
                checkDict[checkNode.dataval] = 1

            #print str(checkNode.dataval) + " has occurences " + str(checkDict[checkNode.dataval])
            checkNode = checkNode.nextval


        # now use that list to identify dupes
        checkNode = self.headval
        while checkNode is not None:
            # use hash lookup
            if checkDict[checkNode.dataval] > 1:
                # check for special case where the root node's value is in another node
                if checkNode == self.headval:
                    # make the second node the root 
                    self.headval = checkNode.nextval
                else:
                    # check for case where any other node's value is in another node
                    # set previous node to point to next node, thus dropping current node into the ether
                    prevNode.nextval = checkNode.nextval
                # decrement the checkDict hash value since we removed a node
                checkDict[checkNode.dataval] -= 1
            else:
                # if we didn't delete a node, set the previous node value to the current node we just looked at
                prevNode = checkNode

            # then set checkNode to the next node in the list
            checkNode = checkNode.nextval


    def findMiddleNode(self, headNode):
        # set both iterators to root node
        oneATAT = twoATAT = headNode
        # move through the list - one iterator one node at a time, the other two at a time
        # the slower iterator ends up in the middle
        while twoATAT.nextval is not None and twoATAT.nextval.nextval is not None:
            oneATAT = oneATAT.nextval
            twoATAT = twoATAT.nextval.nextval
        return oneATAT
    
    def mergeSort(self, headNode):
        if headNode is None or headNode.nextval is None:
            return headNode

        midNode = self.findMiddleNode(headNode)
        next2midNode = midNode.nextval
        # cut list in half
        midNode.nextval = None
        
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
            result.nextval = self.merge(a.nextval, b)
        else:
            result = b
            result.nextval = self.merge(a, b.nextval)

        return result
        
        

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


#######################

sl = SLinkedList()
sl.headval = sl.Node(1)
sl.listprint()
sl.appendNode(4)
sl.appendNode(2)
sl.appendNode(3)
sl.appendNode(15)
sl.appendNode(5)
sl.appendNode(5)
sl.appendNode(5)
sl.appendNode(14)
sl.appendNode(14)
sl.appendNode(13)
sl.appendNode(14)
sl.appendNode(14)
sl.appendNode(4)
sl.appendNode(5)
sl.appendNode(5)
sl.appendNode(5)
sl.appendNode(4)
sl.appendNode(10)
print "----------- Initial List ------------"
sl.listprint()
print "----------- Removed Dulicates ------------"
sl.pruneDupes()
sl.listprint()
print "----------- Middle of List ------------"
print str(sl.findMiddleNode(sl.headval).dataval)
print "----------- Sorted List ------------"
sl.mergeSort(sl.headval)
sl.listprint()
