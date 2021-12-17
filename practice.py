# n=int(input("enter any number"))
# i=2
# j=0
# while i<=n/2:
#     if n%2==0:
#         j=1
#     i+=1
# if j==0:
#     print("it is a prime number")
# else:
#     print("it is not a prime number")
n=int(input("enter the number"))
i=2
j=0
while i<=n:
    if n%2==0:
        j=1
    i+=1
if n==0:
    print("it is a prime number")
else:
    print("it is not a prime number")