execfile("/Users/jmortko/src/testing/linkedListClass.py")
execfile("/Users/jmortko/src/testing/treeClass.py")

def listFromTree(tree):
    if tree is None:
        return
    h = tree.height(tree)
    for i in range(1, h+1):
        l = listAtLevel(tree, None, i)
        print "List at level " + str(i)
        l.listprint()
        print "\n"

def listAtLevel(tree, sl, level):
    if tree is None:
        return
    # create a linked list here with each node from this level
    if sl is None:
        sl = SLinkedList()
    if level == 1:
        sl.headval = sl.Node(tree.data)
        print "level 1 ..."
        sl.listprint()
    elif level > 1 :
        print "level " + str(level) + " ... "
        sl = listAtLevel(tree.left, sl, level-1)
        sl.listprint()
        sl.headval.nextval = listAtLevel(tree.right, sl, level-1)
        sl.listprint()
    return sl


    


########

root = Tree(5)
root.insert(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(1)
root.insert(4)

root.drawTree(root)

lfromt = listFromTree(root)





