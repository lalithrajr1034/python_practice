#Binary search tree

def BinarySearch(array, number):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == number:
            
            return print("This is a best case:", array[mid])
        elif array[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return -1

array = [5, 75, 3, 46, 53, 89, 3, 56, 6, 97, 6, 77]
array.sort()
print("Sorted array:", array)
number = int(input("Enter the number to search: "))
BinarySearch(array, number)
