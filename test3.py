n=int(input())
listt=list(map(int,input().split()))
depth=1
print(depth,end=" ")
j=1
while j<n-1:
    if listt[j]<=listt[j-1]:
        depth+=1
        print(depth, end=" ")
    else:
