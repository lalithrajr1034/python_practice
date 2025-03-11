def lis(li,ind):
    if ind==0:
        return 0
    v=lis(ind-1)
    print(li[v])
    

lli=[2,3,5,76,87,5]    
a=len(lli)
lis([2,3,5,76,87,5],a)

