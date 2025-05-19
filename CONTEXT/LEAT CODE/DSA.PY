# QUEUE

# Frount(first 0r Head) and Rare(last or tail) 
# insert(enqueue) and delete(dequeue)

# DRAW BACK:
# simply there is a wastage of a space [empty,emp,emp,emp,5] exept last element space there is a memory wastage 
# we can use circular queue for queue dis advantage

class queue:
    lis=[]
    def __init__(self)->None:
                
        self.enqueue=-1
        self.dequeue=-1

    def Info(self):
        if len(self.lis)==self.enqueue:
            print("queue is over flow")
        elif self.enqueue and self.enqueue == -1:
            print("queue is underflow")
    def Add_element(self,size,element):
        if self.enqueue==size and self.dequeue==size:
            print("Queue is overflow")
        self.enqueue=self.enqueue+1         
        self.lis.append(element) 
        print(self.lis)
    print(lis)           
    def Del_element(self):
        if self.enqueue and self.dequeue==-1:
            print("Queue is underflow")
        else:
            self.dequeue=self.dequeue+1     
            self.lis.pop()
    def Print_element(self):
        print(self.lis)            


size=int(input("say the size"))

obj=queue()
obj.Info()
obj.Add_element(size,input("enter the element to add"))
obj.Add_element(size,input("enter the element to add"))
obj.Add_element(size,input("enter the element to add"))

# obj.Del_element()    
# obj.Print_element()

