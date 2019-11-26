# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data, payload):
		self.data = data
		self.payload = payload
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.data)

# Recursive function to check if two given binary trees are identical or not
def isIdentical(root1, root2):
	# If both tree is null return true
	if not root1 and not root2:
		return True

	# if both trees are non-empty and value of their root node matches,
	# recur for their left and right sub-tree
	if (root1 and root2) and (root1.data == root2.data) :
		return isIdentical(root1.left, root2.left) and \
			   isIdentical(root1.right , root2.right)
	else:
		return False

if __name__ == '__main__':
	root1 = Node(1, "Ann")
	root1.left = Node(2, "Bee")
	root1.right = Node(3, "Cee")
	root1.left.left = Node(4, "Dee")
	root1.left.right = Node(5, "Fee")
	root1.left.right.left = Node(8, "Gee")
	root1.left.right.left.left = Node(9, "Hee")
	root1.left.right.left.left.left = Node(10, "Iee")
	root1.right.right = Node(7, "Jeea")
	root1.right.right.right = Node(11, "Kilo")

	root2 = Node(1, "Ann")
	root2.left = Node(2, "Bee")
	root2.right = Node(3,"Cee")
	root2.left.left = Node(4, "Dee")
	root2.left.right = Node(5, "Fee")
	root2.left.right.left = Node(8, "Gee")
	root2.left.right.left.left = Node(9, "Hee")
	root2.left.right.left.left.left = Node(10, "Iee")
	root2.right.right = Node(7, "Jeea")
	root2.right.right.right = Node(11, "Kilo")

	print("root1 and root2 are Identical " if isIdentical(root1, root2)
		  else "root1 and root2 are not Identical ")

	root1.right.right.right = Node(12, "touhy")
	print("root1 and root2 are Identical " if isIdentical(root1, root2)
		  else "root1 and root2 are not Identical ")

