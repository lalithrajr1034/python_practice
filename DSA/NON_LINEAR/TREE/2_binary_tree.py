class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right= None


a = Node(4)
a.left = Node(5)
a.right = Node(6)


print(a.left.data)
a.left.right = Node(2)

# print(id(a.data))
# print(id(a.left))


def smallestNumber(n, t):
    a = n%10
    if a%t ==0:
        return n
    return smallestNumber(n+1, t)

print(smallestNumber(15,3))
        