import numpy as np
N=int(input())
for case in range(N):
    l,h,n,d1,d2=map(int,input().split())
    lined1 = int((d1-n) / l)
    colomnd1 = (d1-n) % l
    lined2 = int((d2-n) / l)
    colomnd2 = (d2-n) % l
    res=0
    A = np.arange(n, n+l*h).reshape(h, l)
    if colomnd1<colomnd2:
        A[lined1:lined2 + 1, colomnd1:colomnd2 + 1] = 0
    else:
        A[lined1:lined2 + 1, colomnd2:colomnd1 + 1] = 0
    A = list(A.flatten())
    for i in A:
        if i!=0:
            res = res ^ i
    print(res)
