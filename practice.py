i=1
while i<=5:
    j=1
    while j<=i:
        if i==2:
            print("*",end=" ")
        elif i==4:
            print("*",end=" ")
        else:
            print(j,end=" ")
        j+=1
    i+=1
    print()
