import math


n,k=map(int,input().split())
listt=list(map(int,input().split()))
resSet=set(listt)
for i in range(0,n-1):
    for j in range(i+1,n):
        if listt[j]%listt[i]!=0:
            resSet.add(math.gcd(listt[i],listt[j]))
print(len(resSet))