N=int(input())
dic={}

for i in range(1,N+1):
    nb,lor=input().split()
    if nb not in dic.keys():
        if lor=='L':
            dic[nb]=[1,0]
        else:
            dic[nb] = [0, 1]
    else:
        if lor=='L':
            dic[nb]=[dic[nb][0]+1,dic[nb][1]]
        else:
            dic[nb] = [dic[nb][0] , dic[nb][1]+1]
s=0;
for val in dic.values():
    s+=min(val)
print(s)