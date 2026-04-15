from calc_art import art
print("WELCOME TO CALCULATOR")
print(art)
def menu(x):
    if x=='1' or x=="add":
        a = input("add first number")
        b = input("add second number")
        add(a,b)
        
    
def add(x: int, y: int):
    print(f"{x} + {y} = {x+y}")

def subtract(x: int, y: int):
    print(f"{x} - {y} = {x-y}")

def multiply(x: int, y: int):
    print(f"{x} X {y} = {x*y}")

def divide(x: int, y: int):
    print(f"{x} / {y} = {x/y}")

def computer():
    while True:
        

