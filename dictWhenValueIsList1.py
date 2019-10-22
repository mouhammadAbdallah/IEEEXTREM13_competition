N=int(input())
dic={}
for i in range(0,N):
    s,h=input().split()
    h=int(h)
    if h not in dic.keys():
        templist=[s]
        dic[h]=templist
    else:
        templist=list(dic[h])
        templist.append(s)
        dic[h]=templist
rank=1;
for key in sorted(dic.keys()):
    lis=list(dic[key])
    lis.sort()
    print(*lis,end=' ')
    print(rank,end=" ")
    rank=rank+len(dic[key])-1
    print(rank)
    rank+=1
