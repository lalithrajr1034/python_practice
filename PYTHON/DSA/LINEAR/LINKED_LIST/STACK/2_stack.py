def Stack():
    List=[]
    print("""
             1 create add element
             2 for add element
             3 delete an element""")
    option=int(input("Enter your option "))
    if  option==1:
        Insert=int(input("Enter the number of elements to insert"))
        for i in range(0,Insert):
            element=int(input())
            List.append(element)
        print(List)   
    if  option==2:
        Insert=int(input("Enter still remaining elements to insert"))
        for i in range(0,Insert):
            element=int(input())
            List.append(element)
        print(List)    
    if  option==3:
        leng_of_lis=len(List)-1
        List.pop(leng_of_lis)

    
    
Stack()