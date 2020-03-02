
class Tree:
    def __init__(self, data, left=None, right=None, isRoot=True):
        self.left = left
        self.right = right
        self.data = data
        self.isRoot = isRoot


    def insert(self, data):
        # this inserts into a binary search tree
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


    def isBinarySearchTree(self):
        # if there is a left node
        if self.left:
            # if the data in this node is larger than the value on the left
            # call this function recursively from the left.node
            # otherwise return False
            if self.data > self.left.data:
                self.left.isBinarySearchTree()
            else:
                return False
        if self.right:
            # if the data in this node is larger than the value on the right
            # call this function recursively from the right.node
            # otherwise return False
            if self.data < self.right.data:
                self.right.isBinarySearchTree()
            else:
                return False

        # return True if it makes it through all of that
        return True


    def depthFirst(self, order):
        # Preorder : root first, then left side,  right side
        # In order : left side first, then root, right side
        # Postorder : left side first, then right side, root
        if order == 'preorder':
            print(self.data)
            if self.left:
            	self.left.depthFirst(order)
            if self.right:
                self.right.depthFirst(order)
        elif order == 'inorder':
            if self.left:
             	self.left.depthFirst(order)
            print(self.data)
            if self.right:
                self.right.depthFirst(order)
        elif order == 'postorder':
            if self.left:
            	self.left.depthFirst(order)
            if self.right:
                self.right.depthFirst(order)
            print(self.data)
        else:
            print('Invalid Order')


    def bTreeSearch(self, lkpval):
        # works for binary search trees only
        print("Traversing the node with data : " + str(self.data))
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
            # if node is None we've reached the end of recursion so return 0
            return 0
        # return the sum of node.data + 
        # the result of calling this method with node.left
        # the result of calling this method with node.right
        return node.total(node.left) + node.total(node.right) + node.data

   
    def isTreeBalanced(self):
        # a binary tree is balanced if the absolute value of (the height of its left side
        # minus the height of its right side) is not greater than 2
        if abs(self.height(self.left) - self.height(self.right)) > 2:
            return False
        else:
            return True

    def height(self, node):
	# return 0 to terminate traversing the tree recursively
        if node is None:
            return 0
        else:
            # OR
            # recursive calls to compute the height of left and right sides of the tree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            # return the larger height of the two
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def drawTree(self, root):
        # get height and loop over that value
        h = self.height(root)
        for i in range(1, h+1):
            # inside the loop call printGivenLevel method 
            self.printGivenLevel(root, i)
            print("\n")


    # Print nodes at a given level
    def printGivenLevel(self, root , level):
        if root is None:
            # if root is None just return to end any recursion
            return
        # get the height of the tree
        tabMultiplier = self.height(root)
        # if we are at level 1 print the value of the node
        if level == 1:
            cnt = 1
            while cnt <= tabMultiplier:
                print("\t",end =" ")
                cnt += 1
            print(str(root.data), end =" ")
        elif level > 1 :
            # else 
            # call this method against root.left and one level lower
            # call this method against root.right and one level lower
            self.printGivenLevel(root.left , level-1)
            self.printGivenLevel(root.right , level-1)
        


    def printSortedTree(self):
	# inorder
        if self.left:
            self.left.printSortedTree()
        print(self.data),
        if self.right:
            self.right.printSortedTree()

    def returnSortedTree(self, arr):
	# inorder
        if self.left:
            self.left.returnSortedTree(arr)
        arr.append(self.data)
        if self.right:
            self.right.returnSortedTree(arr)

    def findNextInOrder(self, checkVal):
        arr = list()
        self.returnSortedTree(arr) 
        i = 0
        while i < len(arr) - 1:
            if arr[i] == checkVal:
                return arr[i+1]
            i += 1
        return str(checkVal) + " is the highest value in the tree"

### end class code ###

def areIdentical(root1, root2):
    # traverse both trees simultaneously
    # if both tree roots are None return True
    if root1 is None and root2 is None:
        return True
    # if one is None and the other isn't , return False
    elif root1 is None or root2 is None:
        return False
    else:
         # otherwise if both nodes data are equal and the result of recursive calls to this method
         # passing in left sides of both trees AND's with calls to the right sides of both trees
         return (root1.data == root2.data and \
                areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right))

def isSubTree(root, subTree):
    # processing both trees at once (root, SubTree)
    # subTree will always be equal or smaller in size 
    if subTree is None:
        # if subTree is None return True since we got to the bottom of it and need to end recursion
        return True
    if root is None:
        # we got to the end of the root tree but SubTree still has values so return False
        return False 

    # use call to areIdentical method to validate whether we've got any matches between the two trees
    if areIdentical(root, subTree):
        return True

    # traverse both sides of the larger tree by calling it as an OR'd recusive invocation of 
    # this method against its left and right sides 
    return isSubTree(root.left, subTree) or isSubTree(root.right, subTree)
 

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
# these lines will break the binary search tree formation
#extra = Tree(1)
#root.right = extra

print("Print Sorted Tree")
root.printSortedTree()
print("\n")

ttl = root.total(root)
print("\nTotal of all node values : " + str(ttl))

print("\nBF Search")
print(root.bTreeSearch(100000))

print("\nDepth First Search in-order")
root.depthFirst(order='inorder')
print("\nDepth First Search pre-order")
root.depthFirst(order='preorder')
print("\nDepth First Search post-order")
root.depthFirst(order='postorder')

print("\nIs tree balanced : " + str(root.isTreeBalanced()))

print("\n")
root.drawTree(root)

print("\n")
print("Is this a binary search tree?")
if root.isBinarySearchTree():
    print("Yes")
else:
    print("No")

arr = list()
root.returnSortedTree(arr)
print("Sorted Tree " + str(arr))

checkVal = 4
print("Finding next inorder for " + str(checkVal))
print(str(root.findNextInOrder(checkVal)))

st = Tree(3)
st.insert(1)
st.insert(4)

st.drawTree(st)

if isSubTree(root, st):
    print("Yes - we have a subtree")
else:
    print("No - we do not have a subtree")
