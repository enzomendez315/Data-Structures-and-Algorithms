"""
Implementation for a singly linked list.
"""

class Node:
    def __init__(self, value) -> None:
        """Constructs a Node."""
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        """Constructs a LinkedList."""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        """Inserts an item at the end of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value) -> bool:
        """Inserts an item at the beginning of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        """Removes the item at the end of the list."""
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self) -> Node:
        """Removes the item at the beginning of the list."""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def print_list(self) -> None:
        temp = self.head
        while temp.next is not None:
            print(temp.value, " -> ")
            temp = temp.next
        print(temp.value)