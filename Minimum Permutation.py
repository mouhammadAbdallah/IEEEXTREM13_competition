import numpy as np

n,m=map(int,input().split())
listt=np.asarray(list(map(int,input().split())))
sett=list(map(int,input().split()))
sett.sort()


for i in sett:
    arr=listt-i
    l=len(arr)
    j=0
    while arr[j]<0 and j< l:
        j+=1

    if j<l:
        listt=np.insert(listt,j,i)
    else:
        listt=np.append(listt,j)



print(" ".join(map(str, listt)))
