def smallestNumber(n, t):
    a = n%10
    if a%t ==0:
        return n
    return smallestNumber(n+1, t)

print(smallestNumber(15,3))
        