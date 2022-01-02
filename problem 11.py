n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=i:
        # print(i*i,end=" ")
        print(pow(i,2),end=" ")
        j+=1
    i+=1
    print()