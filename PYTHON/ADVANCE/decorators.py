#Decorators is the function which receive a funcion as input and add some functionality(decoration's) and return a function

def decorator(a):
    def wrapper():
        print("**********")
        a()
        print("**********")
    return wrapper
def sec(n):
    print("my name is lalith raj",n)
a = decorator(sec) 
a()

# or

@decorator
def lalith():
    print("My name is lalith raj r")
lalith()    
#--------------------------------------------------------------------------------


@decorator
def sec(n):
    print("my name is lalith raj", n)

#this both are same 
def sec(n):
    print("my name is lalith raj", n)
sec = decorator(sec)


#---------------------------------------------------------------------------------
import time

def time_decorator(ti):
    def wrappor():
        start = time.time()
        ti()
        end   = time.time()
        print("Time taken to execute a function is ",end-start)
    return wrappor

@time_decorator
def lal():
    for i in range(201):
        print(i)
lal()            

@time_decorator
def lal():
    for i in range(201):
        print("Time taken to exectue a function is ",i)
lal()            


#----------------------------------------------------------------------------------
def decorator(a):
    def wrapper(*z):
        print("**********")
        a(*z)
        print("**********")
    return wrapper
@decorator   #sec = decorator(sec)
def sec(n):
    print("my name is lalith raj",n)
sec("hi lalith")




#-----------------------------------------------------------
# Advanced Topic
def tablet(data_type):
    def decorator(fun):
        def wrapper(*args):
            if type(args[0]) == data_type:
                print("this is correct data type ")    
                print("************************")
                fun(*args)
                print("*************************")                
            else:
                raise TypeError (" data type is not correct ")      

        return wrapper
    return decorator

def functions(a):
    print(a*2)
    
functions = tablet(str)(functions)     #here we can change a type of a data with respect to pareameters   
functions("lalith ")