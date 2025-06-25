a=3
def enclosed_name():
    print("this is a enclosednamespace")
    def local_name():
        a=1
        print(a)  
    return local_name()
enclosed_name() 