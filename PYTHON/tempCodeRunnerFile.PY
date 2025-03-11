def sum(inpu):
    if inpu==1:
        return 1
    return sum(inpu-1) + inpu

na=int(input())
g=sum(na)
print(g)    