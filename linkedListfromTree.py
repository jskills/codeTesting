
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

class Tree:
    def __init__(self, data, left=None, right=None, isRoot=True):
        self.left = left
        self.right = right
        self.data = data
        self.isRoot = isRoot


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data, isRoot=False)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data, isRoot=False)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def depthFirst(self):
        print(self.data)
        if self.left:
           self.left.depthFirst()
        if self.right:
            self.right.depthFirst()


    def bTreeSearch(self, lkpval):
        # works for binary trees only
        print "Traversing the node with data : " + str(self.data)
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.bTreeSearch(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.bTreeSearch(lkpval)
        else:
            print(str(self.data) + ' is found')


    def total(self, node):
        # assumes integer data values
        if node == None: 
            return 0
        print "looking at node with data : " + str(node.data)
        return node.total(node.left) + node.total(node.right) + node.data

   
    def isTreeBalanced(self):
        if abs(self.height(self.left) - self.height(self.right)) > 2:
            return False
        else:
            return True

    def height(self, node):
        if node is None:
            return 0
        else :
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            #Use the larger one
            if lheight > rheight :
                return lheight+1
            else:
                return rheight+1

    def drawTree(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.printGivenLevel(root, i)
            print "\n"


    # Print nodes at a given level
    def printGivenLevel(self, root , level):
        if root is None:
            return
        thisHeight = self.height(root)
        tabMultiplier = thisHeight
        if level == 1:
            cnt = 1
            while cnt <= tabMultiplier:
                print "\t",
                cnt += 1
            print str(root.data),
        elif level > 1 :
            self.printGivenLevel(root.left , level-1)
            self.printGivenLevel(root.right , level-1)
        


    def printSortedTree(self):
        if self.left:
            self.left.printSortedTree()
        print( self.data),
        if self.right:
            self.right.printSortedTree()



###################################

def listFromTree(tree):
    if tree is None:
        return
    h = tree.height(tree)
    for i in range(1, h+1):
        print "List at level : " + str(i)
        l = listAtLevel(tree, None, i)
        l.listprint()
        print "\n"

def listAtLevel(tree, sl, level):
    if tree is None:
        return
    # create a linked list here with each node from this level
    if sl is None:
        sl = SLinkedList()
    if level == 1:
        if sl.headval is None:
            sl.headval = sl.Node(tree.data)
        else:
            sl.appendNode(tree.data)
    elif level > 1 :
        if sl.headval is None:
            sl = listAtLevel(tree.left, sl, level-1)
        else:
            listAtLevel(tree.left, sl, level-1)
        listAtLevel(tree.right, sl, level-1)
    return sl


########

root = Tree(50)
root.insert(120)
root.insert(60)
root.insert(140)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(10)
root.insert(25)
root.insert(35)
root.insert(45)
root.insert(55)
root.insert(65)
root.insert(130)
root.insert(150)

root.drawTree(root)

lfromt = listFromTree(root)





