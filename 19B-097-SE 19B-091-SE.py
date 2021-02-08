import random
# importing random module for generating Random Priority Values

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.priority = None

        # generate random numbers for heap priority
        if self.priority is None:
            self.priority = random.randint(0, 250)

class RandomBinarySearchTree:
    # initialize parent pointer as nil
    def __init__(self):
        self.root = None

    def Rotate_left(self, root):
        """This function will rotate the root node to the left side"""
        r = root.right
        x = root.right.left

        # rotate
        r.left = root
        root.right = x

        # set root
        return r

    def Rotate_right(self, root):
        """This function will rotate the root node to the right side"""
        l = root.left
        y = root.left.right

        # rotate
        l.right = root
        root.left = y

        # set root
        return l

    # wrapper function
    def Insert(self, value):
        self.root = self.__Insert(self.root, value)

    def __Insert(self, root, value):
        # check if tree is empty
        # base case
        if root is None:
            # creates a new node
            root = Node(value)
            return root

        else:
            # if the value is greater than root node, insert in the right subtree
            if value > root.value:
                # recursive call
                root.right = self.__Insert(root.right, value)

                if root.right.priority > root.priority:
                    # left rotation to maintain heap property
                    root = self.Rotate_left(root)

            # else insert in the left subtree
            else:
                # recursive call
                root.left = self.__Insert(root.left, value)

                if root.left.priority > root.priority:
                    # right rotation to maintain heap property
                    root = self.Rotate_right(root)
        return root

    # wrapper function
    def Search(self, value):
        return self.__Search(self.root, value)

    def __Search(self, root, value):
        # base case
        # if the required key is not available in the tree
        if root is None:
            return False

        if root.value == value:
            return True

        # if the required value is greater than root, search in right subtree
        if value > root.value:
            return self.__Search(root.right, value)
        # else search in the left subtree
        return self.__Search(root.left, value)

    def InOrder(self):
        return self.__InOrder(self.root)

    # LVR = Left, Visit, Right
    def __InOrder(self, root):
        if root:
            self.__InOrder(root.left)
            print(f'Value: {root.value} \tPriority: {root.priority}')
            self.__InOrder(root.right)

    def PreOrder(self):
        return self.__PreOrder(self.root)

    # VLR = Visit, Left, Right
    def __PreOrder(self, root):
        if root:
            print(f'Value: {root.value} \tPriority: {root.priority}')
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)

    def PostOrder(self):
        return self.__PostOrder(self.root)

    # LRV = Left, Right, Visit
    def __PostOrder(self, root):
        if root:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(f'Value: {root.value} \tPriority: {root.priority}')

    def Height(self):
        return self.__Height(self.root)

    def __Height(self, root):
        if root is None:
            return 0
        else:
            # recursive call
            left_height = self.__Height(root.left)
            right_height = self.__Height(root.right)
            
            # extract max height
            # then return max height + 1
            # here 1 is added because of root node
            return 1 + max(left_height, right_height)

    def FindMin(self):
        return self.__FindMin(self.root)

    def __FindMin(self, root):
        if root is None:
            return 0
        else:
            while root.left is not None:
                if root.left is None:
                    break
                root = root.left
            return root

    def FindMax(self):
        return self.__FindMax(self.root)

    def __FindMax(self, root):
        if root is None:
            return 0
        while root.right is not None:
            if root.right is None:
                break
            root = root.right
        return root

    def Delete(self, value):
        return self.__Delete(self.root, value)

    def __Delete(self, root, value):
        if root is not None:
            if root.value == value:
                if root.left is None and root.right is None:
                    return None

                # Case 1: node to be deleted is a leaf node
                else:
                    if root.left is None:
                        return root.right
                    elif root.right is None:
                        return root.left

                    # case 2: when the value to be deleted has two childrens
                    else:
                        if root.right.priority > root.left.priority:
                            self.Rotate_left(root)
                            root.left = self.__Delete(root.left, value)
                        else:
                            self.Rotate_right(root)
                            root.right = self.__Delete(root.right, value)

            elif value < root.value:
                root.left = self.__Delete(root.left, value)
            elif value > root.value:
                root.right = self.__Delete(root.right, value)
        return root

# for testing results
def Test():
    rbst = RandomBinarySearchTree()
    rbst.Insert(20)
    rbst.Insert(2)
    rbst.Insert(1)
    rbst.Insert(7)
    rbst.Insert(12)
    rbst.Insert(13)
    rbst.Insert(15)
    rbst.Insert(18)

    print('\nPreOrder')
    rbst.PreOrder()

    print('\nPostOrder')
    rbst.PostOrder()


    print('\nInOrder')
    rbst.InOrder()
    rbst.Delete(15)

    print('\nInOrder')
    rbst.InOrder()

Test()