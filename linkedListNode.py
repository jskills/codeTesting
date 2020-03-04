class linkedListNode:
	def __init__(self, data, isRoot=False):
		self.data = data
		self.nextNode = None

	def append(self, data):
		if self.nextNode:
			self.nextNode.append(data)
		else:
			self.nextNode = linkedListNode(data)

	def printList(self, node):
		print(node.data)
		if node.nextNode:
			self.printList(node.nextNode)



#################################

lln = linkedListNode(20, True)
lln.append(40)
lln.append(60)
lln.append(50)
lln.append(80)
lln.append(99)

lln.printList(lln)

