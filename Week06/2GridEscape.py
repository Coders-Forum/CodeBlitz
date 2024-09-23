h,w=map(int,input().split())
k=int(input())
park=[]
for _ in range(h):
    park.append(list(input()))
current=k  
flag=0
if(h==0 or w==0):
    flag=1
else:

    for i in range(h):
        for j in range(w):

            if(current<0):
                flag=1
            if(park[i][j]=="S"):
                continue
            elif(park[i][j]=="E"):
                break
            elif(park[i][j].isdigit()):
                current+=int(park[i][j])-1

            else:
                current-=1
if(flag):
    print(-1)
else:
    print(current-1)
