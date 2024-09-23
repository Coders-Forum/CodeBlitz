k=int(input())
n=int(input())
m=int(input())

page=0
lines=0
i=k
while(lines<n):
    if(i!=6):
        page+=1
        lines+=m
        i+=1
    else:
        i=1
        lines+=(m*2)
        page+=1
print(page)


        
        
