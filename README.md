# Random-Binary-Search-Tree
DSA Group Project
RANDOM BINARY SEARCH TREE
Random Binary Search tree (Treap) is a Balanced Binary Search Tree, but not guaranteed to have height as O (Log n). The idea is to use Randomization and Binary Heap property to maintain balance with high probability. The expected time complexity of search, insert and delete is O (Log n).

FUNCTION USED IN THE BINARY SEARCH TREE:
•	Rotate left (root). 
•	Rotate right (root)
•	Insertion (value)
•	Search(value)
•	Delete (value)
•	InOrder ()
•	PostOrder()
•	PreOrder()

ROTATE RIGHT:
If the value is less than the root than we will we rotate it right.
ROTATE LEFT:
If the value is greater than the root than we will we rotate it left.

INSERTION ():
•	Insert takes value as parameter and insert these values along with random generated priority to maintain maximum heap property. 
If the value is less than the root than it will insert it in the left subtree by using right rotation. And if the value is greater than the root then it will insert it in the right subtree using left rotation.
•	The time complexity is O (log n).
SEARCH ():
•	Search function will take value as parameter.
•	If the required value is greater it will search in the right subtree otherwise if it smaller than the root node then it will search in the left subtree
•	The time complexity is O (log n).
DELETE ():
Delete function will value as parameter.
•	There are three cases in Delete:
•	If the value is a leaf node then delete it.
•	If the value to be deleted has one child.
•	If the value to be deleted has two children.
Time Complexity is O (Log n)
