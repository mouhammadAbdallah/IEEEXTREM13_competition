alphabet='abcdefghijklmnopqrstuvwxyz'
t=int(input())
for case in range(t):
    n,x=map(int,input().split())
    workingletters=alphabet[0:n]
    infstring=workingletters
    i=len(infstring)-1
    miniword=2
    while i<x:
        j=0
        while j<n**miniword:
            infstring+=
