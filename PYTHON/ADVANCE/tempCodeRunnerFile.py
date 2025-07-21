def decorator(fn):
    def wrapper(*args):
        print("**********")
        fn(*args)
        print("**********")
    return wrapper


def divide(numerator: int, denominator: int):
    answer = numerator/denominator
    return answer
val = decorator(divide)
print(val(2,5))