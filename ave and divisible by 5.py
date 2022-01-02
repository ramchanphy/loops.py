i=1
sum=0
while i<=11:
    weight=int(input("enter the weight number"))
    sum=sum+weight
    i+=1
avg=sum/11
print("average=",avg)
if avg%5==0:
    print("is divisible by 5")
else:
    print("is not divisible")