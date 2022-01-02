n=int(input("enter the number"))
i=1
while i<=n:
    if i%2==0 and i%7==0:
        print("curd")
    elif i%3==0 and i%7==0:
        print(i,"milk")
    elif i%2==0 and i%3==0:
        print(i,"honey")
    elif i%2==0:
        print(i,"cake")
    elif i%3==0:
        print(i,"juice")
    elif i%7==0:
        print(i,"butter")
    else:
        print(i,"choclate")
    i+=1
    