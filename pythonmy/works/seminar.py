# Creating a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Creating a Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Adding elements to the end of the doubly linked list
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Displaying the doubly linked list
    def display(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(current.value)
            current = current.next
        print(elements)

# Creating an instance of the Doubly Linked List
my_list = DoublyLinkedList()

# Appending elements to the doubly linked list
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Displaying the doubly linked list
my_list.display()  # Output: [10, 20, 30]
# Creating a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating a Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Adding elements to the circular linked list
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Displaying the circular linked list
    def display(self):
        current = self.head
        elements = []
        if self.head is not None:
            while True:
                elements.append(current.value)
                current = current.next
                if current is self.head:
                    break
        print(elements)

# Creating an instance of the Circular Linked List
my_list = CircularLinkedList()

# Appending elements to the circular linked list
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Displaying the circular linked list
my_list.display()  # Output: [10, 20, 30]
