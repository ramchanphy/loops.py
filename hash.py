n=int(input("enter the num"))
row=0
while row<n:
    com=row+1
    while com>0:
        print("#",end=" ")
        com-=1
    row+=1
    print()