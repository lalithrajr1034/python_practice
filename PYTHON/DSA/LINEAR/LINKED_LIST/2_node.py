# To work with a linked list first we have to learn how to make a node


# Node is created value is inserted and adress of every node is None 
class Node:
    def __init__(self, value):
        self.data = value 
        self.address = None
obj11 = Node(4)  
obj22 = Node(32)
obj33 = Node(7)

print(id(obj11)) #1692024401808 we have to add the adress in the node   obj1--> obj2--> obj3-->None


#................................................

class Linked:
    def __init__(self, value):
        self.value = value
        self.address = None
obj1 = Linked(4)  
obj2 = Linked(32)
obj3 = Linked(7)

obj1.next = obj2
obj2.next = obj3 
print(obj1.next)  

