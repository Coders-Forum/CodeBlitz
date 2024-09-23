n = int(input())
lst = []
for i in range(n):
    lst.append(input())
result = ""
i = 0
while 1:
    flag = 0
    char = lst[0][i:i+1]
    if(char == ""):
        break
    for j in range(1, n):
        if(char != lst[j][i:i+1]):
            flag = 1
            break
    if(flag == 1):
        break
    result += char
    i += 1
print(result)
