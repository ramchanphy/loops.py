n=int(input("enter the number"))
i=1
while i<=n:
    a=n-1
    while a>=i:
        print(" ",end='')
        a-=1
    j=i
    while j>=1:
        print(j,end='')
        j-=1
    i+=1
    print()
    
# 