# #Time complacity:
#     #It is calculating a mathematical expresion for increse in time taken to execute a program wrto incresing in no of input



# l=[1,2,3,4,5]
# for i in range(0,len(l)//2):
#     other=len(l)-1-i
#     temp=l[i]        #if we remove this it will be  and replace temp by l[i]  [5, 4, 3, 4, 5]
#     l[i]=l[other]
#     l[other]=temp    #if we replace temp with l[i] and past it above 10 and it will be [1, 2, 3, 2, 1]
# print(l)


class Node:
    def __init__(self, value):
        self.value = value
        self.addres= None
class Link:
    def __init__(self):
        self.head = None
        self.count = 0
    def head_add(self, item:int)->None:  
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head
        self.count+=1
    def __len__(self):
        return self.count
    def traversal(self):
        eval = self.head
        while eval!=None:
            print(eval.value)
            eval = eval.next
            return eval
        self.count+=1
obj = Link()
obj.head_add(5)     
obj.head_add(35)        
obj.traversal()    
print(len(obj))      