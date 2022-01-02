row=5
col=5
i=1
while i<=row:
    j=1
    while j<=col:
        if i==1 or i==5 or j==1 or j==5:
            print("3",end=" ")
        elif (i==j==3):
            print("1",end=" ")
        else:
            print("2",end=" ")
        j+=1
    i+=1
    print()
    print()