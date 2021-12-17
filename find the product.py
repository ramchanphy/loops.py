num=int(input("enter the number"))
temp=num
product=1
while (temp!=0):
    product=product*(temp%10)
    temp=int(temp/10)
print("\nproduct of all the digit number",num,":",product)