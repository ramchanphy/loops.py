n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
        j+=1
    print()
    i+=1