a=[]
c=0
for i in range(6):
    a.append(int(input()))
k=int(input())
for i in a:
    if(i>=k):
        c+=1
print(c)
