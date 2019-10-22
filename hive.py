import numpy as np
A = np.matrix('0 1 0 0 0;0 1 0 0 0;0 0 0 1 1;1 0 1 0 0;0 0 0 1 1')
print(A)






def findOne(i,j,itijah):
    if A[i,j]==0 or i<0 or j<0 or i>=A.shape[0] or j>=A.shape[1]:
        return 0
    else:
        if itijah==0:
            return 1+findOne(i,j-1,-1)+findOne(i,j+1,+1)+findOne(i-1,j,+1)+findOne(i-1,j+1,+1)+findOne(i + 1, j+1 ,+1)+findOne(i + 1, j,-1 )
        else:
            if itijah==1:
                return 1+findOne(i,j+1,+1)+findOne(i-1,j,+1)+findOne(i-1,j+1,+1)+findOne(i + 1, j+1 ,+1)
            else:
                return 1+findOne(i,j-1,-1)+findOne(i + 1, j,-1 )
print(findOne(2,3,0))
