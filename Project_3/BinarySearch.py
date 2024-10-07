# Introduction:
# This code defines two classes, TreeNode and BinarySearchTree, to implement a Binary Search Tree (BST).
# A BST is a data structure in which each node has a key. For any given node:
# - The left child node's key is less than the parent node's key.
# - The right child node's key is greater than the parent node's key.
# The BST supports key operations like inserting nodes, searching for nodes, deleting nodes, and traversing the tree in order.

# The TreeNode class represents individual nodes in the tree, while the BinarySearchTree class handles the tree operations.

class TreeNode:
    # The TreeNode class represents a single node in the BST.
    # Each node contains:
    # - key: The value of the node (to be compared during searches or insertions).
    # - left: A pointer/reference to the left child (nodes with values less than the key).
    # - right: A pointer/reference to the right child (nodes with values greater than the key).

    def __init__(self, key):
        # The constructor initializes a TreeNode with a key value.
        # Left and right child pointers are set to None by default because a new node has no children.
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        # This method is used to print the key value when a node is printed.
        return str(self.key)

class BinarySearchTree:
    # The BinarySearchTree class manages the entire tree structure.
    # It has operations to insert nodes, search for nodes, delete nodes, and perform in-order traversal.

    def __init__(self):
        # The constructor initializes an empty tree with the root set to None.
        # The root is the top-most node of the BST, and initially, it's empty.
        self.root = None

    def _insert(self, node, key):
        # This is a recursive helper function to insert a new key into the BST.
        # It takes in a 'node' (which could be the root or any other node) and the key to insert.
        if node is None:
            # If the current node is None (meaning it's an empty spot), a new TreeNode is created and returned.
            return TreeNode(key)

        # If the key to be inserted is smaller than the current node's key,
        # move to the left child (which contains smaller values).
        if key < node.key:
            node.left = self._insert(node.left, key)
        # If the key to be inserted is larger than the current node's key,
        # move to the right child (which contains larger values).
        elif key > node.key:
            node.right = self._insert(node.right, key)
        
        # Once the node is inserted, return the current node back up the recursive call stack.
        return node

    def insert(self, key):
        # This is the public function to insert a new key into the tree.
        # It starts the insertion process from the root.
        # It uses the helper _insert method to recursively find the correct position to insert the new node.
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        # This is a recursive helper function to search for a key in the BST.
        # It takes in a 'node' and the key to search for.
        # It returns the node containing the key if found, otherwise None.

        # Base case: if the node is None (empty tree or reached a leaf) or if the key is found,
        # return the node (or None if not found).
        if node is None or node.key == key:
            return node
        
        # If the key is smaller than the current node's key, search the left subtree.
        if key < node.key:
            return self._search(node.left, key)
        
        # If the key is greater, search the right subtree.
        return self._search(node.right, key)
    
    def search(self, key):
        # This is the public function to search for a key in the tree.
        # It starts the search from the root using the helper _search method.
        return self._search(self.root, key)

    def _delete(self, node, key):
        # This is a recursive helper function to delete a key from the BST.
        # It returns the new subtree with the key deleted, or the same subtree if the key isn't found.

        if node is None:
            # If the current node is None, the key is not found, so return None.
            return node

        # If the key to be deleted is smaller than the current node's key, move to the left subtree.
        if key < node.key:
            node.left = self._delete(node.left, key)
        # If the key to be deleted is greater than the current node's key, move to the right subtree.
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # If the key is found, we need to delete this node.
            
            # Case 1: Node with only one child or no child.
            if node.left is None:
                return node.right  # Return the right child (or None if no children).
            elif node.right is None:
                return node.left  # Return the left child (or None if no children).

            # Case 2: Node with two children.
            # Get the minimum value from the right subtree to replace the node's key.
            node.key = self._min_value(node.right)
            
            # Delete the minimum node from the right subtree (since its value was used to replace the current node).
            node.right = self._delete(node.right, node.key)
        
        # Return the modified subtree back up the recursive call stack.
        return node

    def delete(self, key):
        # This is the public function to delete a key from the tree.
        # It uses the _delete helper function to recursively delete the key from the root.
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        # This helper function returns the minimum key in a subtree.
        # It's used to find the smallest value in the right subtree when deleting a node with two children.

        while node.left is not None:
            # Keep moving left until you find the smallest (left-most) node.
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        # This is a recursive helper function to perform an in-order traversal of the tree.
        # In-order traversal visits nodes in increasing order (left child -> current node -> right child).
        
        if node:
            # Visit the left subtree first.
            self._inorder_traversal(node.left, result)
            # Visit the current node and add its key to the result list.
            result.append(node.key)
            # Visit the right subtree.
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        # This is the public function to perform an in-order traversal of the tree.
        # It returns a list of all the node keys in increasing order.
        result = []
        self._inorder_traversal(self.root, result)
        return result

# Example usage of the BinarySearchTree:

# Create a new BST.
bst = BinarySearchTree()

# Insert multiple nodes into the BST.
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

# Search for the node with key 80.
print('Search for 80:', bst.search(80))

# Perform an in-order traversal of the BST (prints nodes in increasing order).
print("Inorder traversal:", bst.inorder_traversal())

# Delete the node with key 40 from the BST.
bst.delete(40)

# Check if the node with key 40 exists (should be None).
print("Search for 40:", bst.search(40))

# Perform another in-order traversal after deletion.
print('Inorder traversal after deleting 40:', bst.inorder_traversal())