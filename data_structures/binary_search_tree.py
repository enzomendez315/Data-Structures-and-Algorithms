"""
Implementation for a binary search tree.
"""

class BinarySearchTree:
    class __Node:
        """Internal class for the BinarySearchTree class."""
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

        def get_value(self):
            return self.value
        
        def get_left(self):
            return self.left
        
        def get_right(self):
            return self.right
        
        def set_value(self, new_value):
            self.value = new_value

        def set_left(self, new_left):
            self.left = new_left

        def set_right(self, new_right):
            self.right = new_right

        def __iter__(self):
            """Iterates through the nodes using in-order traversal."""
            if self.left != None:
                for node in self.left:
                    yield node

            yield self.value

            if self.right != None:
                for node in self.right:
                    yield node

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts an element in the BST."""

        def __insert(root, value):
            """Recursive static function that does the work."""
            if root == None:
                return BinarySearchTree.__Node(value)
            
            if value < root.get_value():
                root.set_left(__insert(root.get_left(), value))
            else:
                root.set_right(__insert(root.get_right(), value))
            return root

        self.root = __insert(self.root, value)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()





def main():
    s = input("Enter a list of numbers: ")
    numbers = s.split()

    tree = BinarySearchTree()

    for x in numbers:
        tree.insert(float(x))

    for x in tree:
        print(x)

if __name__ == "__main__":
    main()