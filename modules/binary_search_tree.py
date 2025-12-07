from modules.binary_tree import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # BST INSERT
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # SEARCH
    def search(self, node, value):
        if node is None:
            return None
        if value == node.value:
            return node
        elif value < node.value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    # GET MAX VALUE
    def get_max_value(self, node):
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current.value

    # GET MIN VALUE (helper used in deletion)
    def get_min_value(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    # DELETE NODE
    def delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children
            successor_value = self.get_min_value(node.right)
            node.value = successor_value
            node.right = self.delete(node.right, successor_value)

        return node

    # HEIGHT OF NODE
    def get_height_with_path(self, value):
        # Step 1: Find the node in the BST
        target = self.search(self.root, value)
        if target is None:
            return None, []

        # Step 2: Recursive function to compute height AND path
        def _height_and_path(node):
            if node is None:
                return -1, []

            left_h, left_path = _height_and_path(node.left)
            right_h, right_path = _height_and_path(node.right)

            if left_h >= right_h:
                return left_h + 1, [node.value] + left_path
            else:
                return right_h + 1, [node.value] + right_path

        return _height_and_path(target)



