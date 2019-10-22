n=int(input())
if n%2==0:
    print(int(n/4)*'Yy',end="")
    print(int(n/4)*'yY',end="")
else:
    print(int(n / 4) * 'Yy', end="")
    print('Y',end="")
    print(int(n / 4) * 'yY', end="")