def gradingStudents(grades):
    a=[]
    for i in grades:
        if(i<38):
            a.append(i)
        else:
            k=i
            while(k%5!=0):
                k+=1
            
            if((k-i)<3):
                a.append(k)
            else:
                a.append(i)
    return a
