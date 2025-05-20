#Binary search tree
   #it is a type of a Tree in  which it contain lower value's on left side and greater value is in right side


# NOTE: binary search tree dosenot suppert duplicate value
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Reference to next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # Set first node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()  # Output: 10 -> 20 -> 30 -> None
