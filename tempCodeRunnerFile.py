a = [1, 3,  5,  7,  9]
i = 0
c = len(a)
found_even = True  # Flag to check if even numbers exist

while i < c:
    if a[i] % 2 == 0:
        print("Even number:", a[i])
        found_even = False
    i += 1

if found_even:
    print("No even numbers found.")
