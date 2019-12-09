from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None

    def search(self, key):  # returns True if key is in a node of the tree, else False
        is_true = False
        node = self.root
        while not is_true:
            if node is not None:
                if node.key == key:
                    is_true = True
                elif node.key > key and node.left is not None:
                    node = node.left
                elif node.key < key and node.right is not None:
                    node = node.right
                else:
                    return False
            else:
                return False
        return is_true

    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        new_node = TreeNode(key, data)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_helper(key, self.root, new_node)

    def insert_helper(self, key, current, new_node):  # recursively searches for the key and inserts
        if key == current.key:
            current.data = new_node.data
        elif key > current.key:
            if current.right is not None:
                self.insert_helper(key, current.right, new_node)
            else:
                current.right = new_node
        elif key < current.key:
            if current.left is not None:
                self.insert_helper(key, current.left, new_node)
            else:
                current.left = new_node

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.key, current.data)

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return (current.key, current.data)

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None
        height = 0
        height += self.height_helper(self.root)
        return height

    def height_helper(self, node):  # recursively runs through each branch until it finds the largest
        left_height = 0
        right_height = 0
        if node.left is not None:
            left_height = 1 + self.height_helper(node.left)
        if node.right is not None:
            right_height = 1 + self.height_helper(node.right)
        return max(left_height, right_height)

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST
        lst = []
        return self.inorder_helper(self.root, lst)

    def inorder_helper(self, node, lst):  # recursively adds items to the list going through each branch
        if node is not None:
            self.inorder_helper(node.left, lst)
            lst.append(node.key)
            self.inorder_helper(node.right, lst)
        return lst

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        lst = []
        return self.preorder_helper(self.root, lst)

    def preorder_helper(self, node, lst):  # recursively runs through the node left and right branches
        if node is not None:
            lst.append(node.key)
            self.preorder_helper(node.left, lst)
            self.preorder_helper(node.right, lst)
        return lst

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        lst = []
        if self.root is not None:
            q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            lst.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return lst
