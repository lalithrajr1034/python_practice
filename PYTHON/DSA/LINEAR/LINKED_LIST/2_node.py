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

