n,a,d=map(int,input().split())
rest=0.1
while rest<a and rest!=0 and d>=a:
    m=int(n/d)
    rest=n%d
    d=d-1

if rest<a and rest!=0:
    print("NO")
else:
    print("YES")
    d+=1
    if rest != 0:
        print(rest,end=" ")
    for i in range(m):
        print(d,end=" ")
