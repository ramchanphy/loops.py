n=int(input("enter the number"))
i=n
while i>=1:
    print(" "*(5-i),end=" ")
    j=1
    while j<=i:
        print ("*",end=" ")
        j=j+1
    print()
    i=i-1