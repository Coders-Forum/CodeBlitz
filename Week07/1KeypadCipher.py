n=int(input())
x=input()
keypad={'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],'6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}

decrypt=""
for i in x.split("-"):
    if("#" in i):
        decrypt+=(keypad[i[0]][i.count(i[0])-1]).upper()
    else:
        decrypt+=(keypad[i[0]][i.count(i[0])-1])
print(decrypt)
