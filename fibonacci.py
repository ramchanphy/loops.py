n=int(input("enter the number"))
i=0
f=0
s=1
t=0
while i<=n:
    if (i<=0):
        t=1
    else:
        t=f+s
        f=s
        s=t
    print(t,end=",")
    
    i+=1


    

