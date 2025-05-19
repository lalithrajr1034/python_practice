# QUEUE

# Frount(first 0r Head) and Rare(last or tail) 
# insert(enqueue) and delete(dequeue)

# DRAW BACK:
# simply there is a wastage of a space [empty,emp,emp,emp,5] exept last element space there is a memory wastage 
# we can use circular queue for queue dis advantage

class queue:
    def __init__(self)->None:
                
        self.enqueue=-1
        self.dequeue=-1
        self.lis=[]


    def Info(self):
        if len(self.lis)==self.enqueue:
            print("queue is over flow")
        elif self.enqueue==-1 and self.dequeue == -1:
            print("queue is underflow")
    def Add_element(self,size,element):
        if self.enqueue==size and self.dequeue==size:
            print("Queue is overflow")
        self.enqueue=self.enqueue + 1         
        self.lis.append(element) 
        print(self.lis)
    def Del_element(self):
        if self.enqueue==-1 and self.dequeue==-1:
            print("Queue is underflow")
        else:
            self.dequeue=self.dequeue + 1     
            self.lis.pop()
    def Print_element(self):
        print(self.lis)            

size=int(input("say the size :"))



obj=queue()
obj.Info()
for i in range(1,size): 
  obj.Add_element(size,int(input("enter the element to add :")))

del_size=int(input("say how many elements to delete :"))

for i in range(1,del_size+1): 
  obj.Del_element()    
obj.Print_element()

