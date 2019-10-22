t=int(input())

for case in range(t):
    arr=list(input())
    i=0
    res=0
    length=len(arr)
    fin=False
    while fin == False:
        if arr[i+1]==arr[i] :
                i+=1
                continue
        lindex=length-1
        while arr[lindex]!=arr[i] and lindex>i:
            lindex-=1

        if lindex==i:
            i+=1
            if i >= length - 2:
                fin = True
            continue
        if lindex==length-1:
            length-=1
        else:
            aux=arr[i+1]
            arr[i+1]=arr[lindex]
            arr[lindex]=aux
            res+=2
            i+=1

    print(res)




