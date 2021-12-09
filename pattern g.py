# n=int(input("enter the num"))
# i=n
# while i>=1:
#     j=n
#     while j>=i:
#         print(j,end=" ")
#         j-=1
#     print()
#     i-=1
    
    
# num=int(input("enter the number"))
# i=num
# while i>=1:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i-=1   
    
# n=int(input("enter the num"))
# row=0
# while row<n:
#     com=row+1
#     while com>0:
#         print("#",end=" ")
#         com-=1
#     row+=1
#     print()

# num=int(input("enter the num"))

quantity=int(input("enter the quantity:"))
price=int(input("enter the price:"))
total_cost=price*quantity
if total_cost>1000:
    discount=total_cost/100*10
    print("total cost=",total_cost-discount)
else:
    print("no discount",total_cost)
