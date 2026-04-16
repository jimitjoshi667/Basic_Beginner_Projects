from calc_art import art
print("WELCOME TO CALCULATOR")
print(art)

def menu(x):
    terminate = False
    if x=='1' or x=="add":
        a = input("add first number")
        b = input("add second number")
        add(a,b)
        
    elif x=='2' or x=="sub" or x=="subtract":
        a = input("add first number")
        b = input("add second number")
        subtract(a,b)

    elif x=='3' or x=="multiply" or x=="mul":
        a = input("add first number")
        b = input("add second number")
        multiply(a,b)

    elif x=='4' or x=="dov" or x=="divide":
        a = input("add first number")
        b = input("add second number")
        divide(a,b)
    
    elif x=='5' or x=="end":
        terminate = True

        
        
                  


def add(x: int, y: int):
    print(f"{x} + {y} = {x+y}")

def subtract(x: int, y: int):
    print(f"{x} - {y} = {x-y}")

def multiply(x: int, y: int):
    print(f"{x} x {y} = {x*y}")

def divide(x: int, y: int):
    print(f"{x} / {y} = {x/y}")

#def take_input():
#    inp = input("enter your operation")



        

