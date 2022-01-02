
guessing_number=5
i=0
while i<=5:
    n=int(input("enter the number"))
    if n==guessing_number:
        print("you have won the game")
        break
    else:
        print("you still have 4 chance")
    n=int(input("enter the number"))
    if n==guessing_number:
        print("you have won the game")
        break
    else:
        print("you have 3 chance")
    n=int(input("enter the number"))
    if n==guessing_number:
        print("you have won the game")
        break
    else:
        print("you have two chance")
    if n==guessing_number:
        print("you have won the game")
        break
    else:
        print("you have only one chance")
    if n==guessing_number:
        print("you have won the game")
        break
    else:
        print("better luck next time")
        
    i+=1
    