def advanced(data):
    print(data)
    def wrapper(val):
        print(f' this is the advanced topic {val}')
    return wrapper

a = advanced("hi lalith")("my name is lalith")
print(a)