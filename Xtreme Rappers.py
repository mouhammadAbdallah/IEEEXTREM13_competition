k,j=map(int,input().split())
res=0
while (k!=0 and j!=0) and k+j>=3:
    if(k>j):
        k=k-2
        j=j-1
    else:

        j = j - 2
        k = k - 1
    res=res+1
print(res)