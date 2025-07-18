def sanity_check(data_type):
    def outer_wrapper(function):
        def inner_wrapper(*args):
            if type(*args)==data_type:
                print("data type matched")
            else:
                raise TypeError("data type not matched")
        return inner_wrapper
    return outer_wrapper

@sanity_check
def v(m):
    print(m**2)

v(6) 