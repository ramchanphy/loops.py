n=int(input("enter the number"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if (temp==rev):
    print("it is a palindrome!")
else:
    print("it is not a palindrome!")