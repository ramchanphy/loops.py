n=int(input("enter the rows"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end='')
        j-=1
    a=i
    while a>=1:
        print("*",end=" ")
        a-=1
    i+=1
    print()

# n=int(input("enter the number"))
