def decorator(a):
    def wrapper(*z):
        print("**********")
        a(*z)
        print("**********")
    return wrapper
@decorator
def sec(n):
    print("my name is lalith raj",n)
sec("hi lalith")