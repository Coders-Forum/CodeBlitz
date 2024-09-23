n=int(input())
x=input()

if(n==1):
    print(x)
else:
    print(x*n)
    for i in range(n-2):
        print(x+" "*(n-2)+x)
    print(x*n)
