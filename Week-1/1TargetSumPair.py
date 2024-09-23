n=list(map(int,input().split()))
k=int(input())

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(n[i]+n[j]==k):
            print([i,j])
