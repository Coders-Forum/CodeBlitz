n,m=map(int,input().split())
box=[]
for _ in range(n):
    box.append(list(input()))
count=0
i=1
for x in box[1::]:
    if("-" in x and "|" not in x and " " not in x or i==n-1):
        count+=box_count
    elif("-" in x and "|" not in x and " " in x and i!=n-1):
        count+=box_count-1
    elif("-" in x and "|" in x):
        count+=(box_count-1)

    else:
        pipe_count=x.count("|")
        box_count=pipe_count-1 
   
    i+=1
print(count)     
        
