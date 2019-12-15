class Node :
	def __init__(self, key):
		self.data = key
		self.left = None 
		self.right = None 

def printLevelOrder(root):

	if root is None :
		return 

	q = []
	q.append(root)

	while (len(q) > 0):
		print(q[0].data, end = " ")
		node = q.pop(0)

		if node.left is not None:
			q.append(node.left)

		if node.right is not None:
			q.append(node.right)

#Driver Program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print ("Level Order Traversal of binary tree is -")
printLevelOrder(root) 