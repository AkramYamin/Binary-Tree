class Node :
	def __init__(self, key):
		self.data = key
		self.left = None 
		self.right = None 

def printInSpiral(root):
	if root is None:
		return
	s1 = []
	s2 = []

	s1.append(root)
	while not len(s1) == 0 or not len(s2) == 0:
		while not len(s1) == 0:
			node = s1.pop()
			print(node.data, end = " ")
			if node.right is not None :
				s2.append(node.right)
			if node.left is not None :
				s2.append(node.left)

		while not len(s2) == 0:
			node = s2.pop()
			print(node.data, end = " ")

			if node.right is not None :
				s1.append(node.left)
			if node.left is not None :
				s1.append(node.right)
# Driver Code 
if __name__ == '__main__': 
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(7)  
    root.left.right = Node(6)  
    root.right.left = Node(5)  
    root.right.right = Node(4)  
    print("Spiral Order traversal of", 
                    "binary tree is ")  
    printInSpiral(root) 