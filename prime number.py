num=int(input("enter the number"))
i=2
j=0
while i<=num/2:
    if num%i==0:
        j=1
        
    i+=1
if j==0:
    print("it is prime")
else:
    print("it is not prime")
    
    