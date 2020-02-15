
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

root = Tree(5)
root.insert(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(1)
root.insert(4)
root.insert(15)
root.insert(16)
root.insert(17)

print "Print Sorted Tree"
root.printSortedTree()
print "\n"

ttl = root.total(root)
print "\nTotal of all node values : " + str(ttl)

print "\nBF Search"
print(root.bTreeSearch(100000))

print "\nDepth First Search"
root.depthFirst()

print "\nIs tree balanced : " + str(root.isTreeBalanced())

print "\n"
root.drawTree(root)
