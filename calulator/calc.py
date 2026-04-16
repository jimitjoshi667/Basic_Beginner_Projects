from calc_art import art


def menu(x):
    terminate = False
    should_continue = False
    if x=='1' or x=="add":
        a = input("add first number")
        b = input("add second number")
        add(a,b)
        result = add(a,b)
        
    elif x=='2' or x=="sub" or x=="subtract":
        a = input("add first number")
        b = input("add second number")
        subtract(a,b)
        result = subtract(a,b)

    elif x=='3' or x=="multiply" or x=="mul":
        a = input("add first number")
        b = input("add second number")
        multiply(a,b)
        result = multiply(a,b)

    elif x=='4' or x=="dov" or x=="divide":
        a = input("add first number")
        b = input("add second number")
        divide(a,b)
        result = divide(a,b)
    
#    elif x=='5' or x=="end":
        terminate = True


#     else :
#        print("invalid input please enter valid input")

    print("Do you want to coninue with this operation? or calculate the result?\n")
    while True:
        i = input("enter 'continue' or 'y' to conintue and 'no' or 'n' to stop : ")
        if i=="continue" or i=='y':
            should_continue = True
            break
        elif i=="no" or i=='n':
            break
        else:
            print("invalid output")

        


def add(x: int, y: int):
    print(f"{x} + {y} = {x+y}")
    return x+y

def subtract(x: int, y: int):
    print(f"{x} - {y} = {x-y}")
    return x-y

def multiply(x: int, y: int):
    print(f"{x} x {y} = {x*y}")
    return x*y

def divide(x: int, y: int):
    print(f"{x} / {y} = {x/y}")
    return x/y

#def take_input():
#    inp = input("enter your operation")

def game():
    print("WELCOME TO CALCULATOR")
    print(art)
    print("enter 1 or add: add")
    print("enter 2 or sub or subtract: subtract")
    print("enter 3 or mul or multiply: multiply")
    print("enter 4 or div or divide: divide")
    print("enter 5: exit calculator")
    while True:
        inp = int(input("enter your choise: "))
        if inp == 1 or 2 or 3 or 4 or 5:
            break
        else:
            print("invalid input!")
    if inp!=5:
        menu(inp)
    else:
        print("closing calculator thank you")



