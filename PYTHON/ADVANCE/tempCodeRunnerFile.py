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
    print(a**2)
    
functions = tablet(int)(functions)        
functions(5)