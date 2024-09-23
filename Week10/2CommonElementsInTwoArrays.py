l1 = int(input())
l2 = int(input())
a1 = input().split( )
a2 = input().split( )
a = 1
for i in range(0,l1):
    for j in range(0,l2):
        if (a1[i] == a2[j]):
            print(a1[i] , end =" ")
            a = 0
if (a == 1):
    print("No common elements")    
