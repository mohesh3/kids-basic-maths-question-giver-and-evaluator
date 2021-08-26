#importing random function
import random
#taking name of the player
name=input("plese enter your name : ")
print(f"hi {name} choose your choice")


ans=0
tries=0

#addition function
def addition():
    a=random.randint(1,1000)
    b=random.randint(1000,900000)
    global res,ans,tries,name
    print(a,'+',b)
    res=a+b
    while not(ans == res):
        ans=int(input("ans : "))
        tries=tries+1
        if(ans == res):
            print(f"Brilliant -->{name}<--")
            print(f"You Tried {tries} Times")
        else:
            print(f"hey {name} {ans} is wrong please try again")
#substraction function
def substraction():
    a=random.randint(1,1000)
    b=random.randint(1000,900000)
    print("you choosen substraction")
    global res,ans,tries
    print(b,'-',a)
    res=b-a
    while not(ans == res):
        ans=int(input("ans : "))
        tries=tries+1
        if(ans == res):
            print(f"Brilliant -->{name}<--")
            print(f"You Tried {tries} Times")
        else:
            print(f"hey {name} {ans} is wrong please try again")
#multiplication function
def multiplication():
    a=random.randint(1,1000)
    b=random.randint(1000,900000)
    print("you choosen multplication")
    global res,ans,tries
    print(b,'*',a)
    res=b*a
    while not(ans == res):
        ans=int(input("ans : "))
        tries=tries+1
        if(ans == res):
            print(f"Brilliant -->{name}<--")
            print(f"You Tried {tries} Times")
        else:
            print(f"hey {name} {ans} is wrong please try again")
#division function
def division():
    a=random.randint(1,100)
    b=random.randint(1000,900000)    
    print("you choosen division")
    print("please enter up to three decimal digits")
    global res,ans,tries
    print(b,'/',a)
    res=round(b/a,3)
    while not(float(ans) == float(res)):
        ans=float(input("ans : "))
        tries=tries+1
        if(float(ans) == float(res)):
            print(f"Brilliant -->{name}<--")
            print(f"You Tried {tries} Times")
        else:
            print(f"hey {name} {ans} is wrong please try again")

#calling selected function by player
def calling():
    print("\n 1 -> Addition \n 2 -> Substraction \n 3 -> Multiplication \n 4 -> Division \n 5 -> exit or new player  \n")
    choice=int(input("enter your choice : "))
    
    if choice==1:
        addition()
    elif choice==2:
        substraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        division()
    elif choice==5:
        exit()
    else:
        print(f"hi {name}plese enter correct choice")
#asking user to play again or not
calling()
choice=input("if you want to try again y or n : ")
choice=choice.lower()

while (choice == "y" or "n"):
    if choice == "y":
        calling()
    elif choice == "n":
        exit()


print("Thank you")
