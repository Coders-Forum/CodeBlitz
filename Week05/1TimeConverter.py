x,y=map(str,input().split())
t=x.split(":")
h=int(t[0])
m=int(t[1])

if(y=="AM" and h!=12 and h!=1):
    if(m-20>0 and 1<=h<=9):
        pec="0"+str(h)+":"+str(m-20)
    elif(m-20>0):
        pec=str(h)+":"+str(m-20)
    elif(m-20==0 and 1<=h<=9):
            pec="0"+str(h)+":"+"00"
    elif(m-20==0):
            pec=str(h)+":"+"00"
    else:
        i=abs(m-20)
        j=60-i
        pec=str(h-1)+":"+str(j)
elif(y=="AM" and h==12):
    if(m-20>0):
        pec="00"+":"+str(m-20)
    elif(m-20==0):
            pec=str("00")+":"+"00"
    else:
        i=abs(m-20)
        j=60-i
        pec="23"+":"+str(j)
elif(y=="AM" and h==1):
    if(m-20>0):
        pec="01"+":"+str(m-20)
    elif(m-20==0):
            pec="01"+":"+"00"
    else:
        i=abs(m-20)
        j=60-i
        pec="00"+":"+str(j)
else:
    if(y=="PM" and h==12):
        if(m-20>0):
            pec=str(h)+":"+str(m-20)
        elif(m-20==0):
            pec=str(h)+":"+"00"
        else:
            i=abs(m-20)
            j=60-i
            pec=str(h-1)+":"+str(j)
    else:
        if(m-20>0):
            pec=str(h+12)+":"+str(m-20)
        elif(m-20==0):
            pec=str(h+12)+":"+"00"
        else:
            i=abs(m-20)
            j=60-i
            pec=str(h-1+12)+":"+str(j)
print(pec)
