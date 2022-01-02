n=int(input("enter the number"))
num=1
for row in range(1,n):
    for col in range(row):
        print(num,end=" ")
        num=num+1
    print()
    print()