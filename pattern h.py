n=int(input("enter the number"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end='')
        j-=1
    a=1
    while a<=i:
        print(a,end='')
        a+=1
    print()
    i+=1
        
       