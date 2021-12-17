n=int(input("enter the number"))
i=0
f=0
s=0
while i<=n:
    if (i<=0):
        t=1
    else:
        t=f+s
        f=s
        s=t
    print(t,end=",")
    i+=1

# n=int(input("enter the number"))    
# a,b=0,1
# while a<=n:
#     print(a,end=",")
#     a,b=b,a+b
    

