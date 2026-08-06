class node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        
class linked_list:
    def __init__(self, data):
        self.data = data
        self.head = None # second_node_loc
        self.count = 0
        
    def head_append(self, data):
        new_node = node(data)
        new_node.pointer = self.head 
        self.head = new_node
        self.count +=1
    def append(self, data)->None:
        new_node = node(data)
        var = self.head
        while var.pointer != None:
            var = var.pointer    
        var = new_node
        self.count += 1

obj = linked_list(3)
obj.head_append
ob = linked_list(5)
ob.append