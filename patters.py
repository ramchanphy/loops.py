# num=int(input("enter the num"))
# i=1
# while i<=num:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1
    
num=int(input("enter the number"))
i=1
while i<=num:
    j=num
    while j>=i:
        print(j,end=" ")
        j-=1
    print()
    i+=1