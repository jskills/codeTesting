class binTree:
	def __init__(self, val, left=None, right=None):
		self.data = val
		self.left = left
		self.right = right

	def insert(self, val):
		if self.data:
			if self.data <= val:
				if self.right:
					self.right.insert(val)
				else:
					self.right = binTree(val)
			else:
				if self.left:
					self.left.insert(val)
				else:
					self.left = binTree(val)
		else:
			self.data = val

	def DFSearch(self, node, pref):
		# pref can be inorder, preorder, postorder
		if pref == 'inorder':
			if(node.left):
				self.DFSearch(node.left, pref)
			print(node.data)
			if(node.right):
				self.DFSearch(node.right, pref)
		elif pref == 'preorder':
			print(node.data)
			if(node.left):
				self.DFSearch(node.left, pref)
			if(node.right):
				self.DFSearch(node.right, pref)
		elif pref == 'postorder':
			if(node.left):
				self.DFSearch(node.left, pref)
			if(node.right):
				self.DFSearch(node.right, pref)
			print(node.data)
		else:
			print('invalid pref value')
	


###########################################


b = binTree(55)
b.insert(40)
b.insert(60)
b.insert(30)
b.insert(50)
b.insert(70)
b.insert(80)
b.insert(25)

print('inorder')
b.DFSearch(b, 'inorder')
print('preorder')
b.DFSearch(b, 'preorder')
print('post0rder')
b.DFSearch(b, 'postorder')

