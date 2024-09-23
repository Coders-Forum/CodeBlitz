n=list(map(int,input().split()))
list1=[]
set1=set()

for i in range(len(n)):
    ele=n[i]
    if(ele in set1):
        continue
    
    list1.append(ele)
    set1.add(ele)
    for j in range(i+1,len(n)):
        if(ele ==n[j]):
            list1.append(ele)
           
            break
print(list1)
