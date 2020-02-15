
class Graph:
    def __init__(self, data, left=None, right=None, isRoot=True):
        self.left = left
        self.right = right
        self.data = data
        self.isRoot = isRoot

    def addVertex(self, rightVal=None, leftVal=None):
        if rightVal:
            node = Graph(rightVal)
            self.right = node
        if leftVal:
            node = Graph(leftVal)
            self.left = node
        return node 

    def connectVertex(self, rightNode=None, leftNode=None):
        if rightNode:
            self.right = rightNode
        if leftNode:
            self.left = leftNode
            

    def depthFirst(self):
        print(self.data)
        if self.left:
           self.left.depthFirst()
        if self.right:
            self.right.depthFirst()


    # Function to  print level order traversal of tree 
    def printLevelOrder(self, root): 
        h = self.height(root) 
        for i in range(1, h+1): 
            self.printGivenLevel(root, i) 
  
  
    # Print nodes at a given level 
    def printGivenLevel(self, root , level): 
        if root is None: 
            return
        if level == 1: 
            print str(root.data), 
        elif level > 1 : 
            self.printGivenLevel(root.left , level-1) 
            self.printGivenLevel(root.right , level-1) 
  
  
    def height(self,node): 
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

###################################

root = Graph('A')
nodeB = root.addVertex(rightVal='B')
nodeC = root.addVertex(leftVal='C')
nodeD = nodeC.addVertex(rightVal='D')
nodeE = nodeD.addVertex(rightVal='E')
nodeJ = nodeD.addVertex(leftVal='J')



print "Depth First"
root.depthFirst()

print "Breadth First"
root.printLevelOrder(root) 

print "\nHeight of Graph"
print str(root.height(root))
print str(root.height(nodeD))
