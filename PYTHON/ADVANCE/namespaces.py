#  NAMESPACE'S

#A namespace is a set of container that holds a set of names and the object they refers to ,
#namespace is impeimented as a dictionaty where the keys(variavle, function's, class, etc..) and the "value" are corresponding object

"""There are 4 types of NameSpace"""
#1.Builtin Namespace
#2.Global Namespace
#3.Enclosing Namesapce(or Non-local Namespace)
#4.Local Namespace

#ex:
#this is a Global space 
def GlobalNamespace():
    print("this is a GlobalNamespace")
    def EnclosedNamespace():
        print("this is a non local or EnclosedNmaespace")
        def LocalNamespace():
            print("this is a localNamespace")        
        LocalNamespace()
    EnclosedNamespace()    
GlobalNamespace()
#--------------------------------------------

#SCOPE
#Scope will allows us to acess the variable and functions from one namespace to another namespace
#it will follow the LEGB rule first search requires object(valie) in localnamespace, if it dosen't find then search in Encolsednamespace, Globalnamespace, at last it will search in Builtinnamespace

#1
a=3
def acess_global():
    print(a) #It can acess the global variable  

acess_global()     

#2
a=3
def acess_global():
    a+=1
    print(a) #we came to know that we can read the data and can't write it   

acess_global()    

#3
a=3
def acess_global():
    global a
    a+=1
    print(a) # we get the data change in global variable so this is not a good practice  

acess_global()


#4
#due to python follow the LEGB rule so we can use a builtin function name as a  vairable and also a our oun function name
print="lalith"
def max():
    return print
max()#Here max and the print are the predefined functoins so here i came to know that we can change the method name's without searching to builtinNamespace

                #or
def input():
    print("my name is lalith")                
input() #Error is not throughing because we get the function in the globalnamespace    



#5
def enclosed_name():
    a=3
    print("this is a enclosednamespace")
    def local_name():
        nonlocal a #Here we are in the localnamespace to use enclosednamespace   or if we want to write things in a global things we have to use a global
        a+=1
        print(a)  
    return local_name()
enclosed_name()    