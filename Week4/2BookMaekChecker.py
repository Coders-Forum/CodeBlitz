ls = list(map(int,input().split()))
ls.sort()
n = ls[0]
m = ls[1]
if n%2 == 0 and m-n == 1 :
    print('YES')
else:
    print('NO')
