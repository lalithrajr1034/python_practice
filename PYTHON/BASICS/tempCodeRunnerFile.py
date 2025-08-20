def advanced(data):
    print(data)
    val = "fg"
    def wrapper(val):
        print(f' this is the advanced topic {val}')
    return wrapper(val)

advanced("hi lalith")#("my name is lalith")
