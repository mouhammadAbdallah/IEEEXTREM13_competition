n,k,q=map(int,input().split())
listt=list(map(int,input().split()))
aux=listt[::]
for case in range(q):
    todo,l,r=input().split()
    l=int(l)
    r=int(r)
    if todo=='U' or todo=='u':
        listt[l-1]=r
    else:
        for kfois in range(k):
            for i in range(l,r):
                listt[i]=listt[i-1]+listt[i]
        print((listt[r-1])%((10**9)+7))
        listt=aux[:]