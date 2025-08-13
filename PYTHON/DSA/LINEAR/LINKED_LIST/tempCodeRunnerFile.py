
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count= 0
    def __len__(self):
        return self.count
    
    # to add a node infrount of head
    def add_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        
    def traverse(self):
        val = self.head      
        while val!= None:
            print(val.value)
            val = val.next
            
    # all things are but (while val.next!= None)-->.next.next.next        
    def append(self, value):
        last_add = Node(value)     
        if self.head == None:
            self.head = last_add
        else:
            val = self.head
            while val.next != None:
                val = val.next  
            val.next = last_add
        self.count += 1
    def add_between(self, where, value):
        search = self.head
        while search.value != where:
            search = search.next
        if search.value == where:
            new_node = Node(value)
            new_node.next = search.next    
            search.next = new_node  
            self.count+=1   
        else:
            print("Value not found")
    def clear(self):
        self.head = None
        self.count = 0
    def def_head(self):
        self.head = self.head.next
        self.count += -1
    def pop(self):
        count = self.head
        while count.next.next == None:
            count.next = None         
        self.count += -1
        if count.next == None:
            print("Only head is present")
        if self.head == None:
            print("linked list is empty")    
            
obj1 = LinkedList()
obj1.add_head(5)  
obj1.add_head(52)        
obj1.append(567)   
obj1.add_between(52, 100)   
print(len(obj1))
obj1.traverse()
obj1.clear()