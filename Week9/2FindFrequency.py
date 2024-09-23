n=input()
dic={}

for i in n:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
        
for i in sorted(list(set(dic.keys()))):
    print(i+":"+str(dic[i]))
