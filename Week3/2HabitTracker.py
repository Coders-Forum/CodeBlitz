n=int(input())
k=int(input())
arr=list(map(int,input().split()))

streak=0
start=0
x=0
j=0
for i in range(len(arr)):
    if(arr[i]==1):
        x+=1
        f=0
    else:
        if(streak<=x):
            j=i
            f=1
        streak=max(streak,x)
        x=0
if(streak<=x):
    j=len(arr)
streak=max(streak,x)

print(j-1-streak+1+n)
