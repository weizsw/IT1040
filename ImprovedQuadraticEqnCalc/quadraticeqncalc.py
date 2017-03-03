import math


def getQuadra(a, b, c):
    a = float(a)
    if a == 0:
        return "0"
    b = float(b)
    c = float(c)
    b = b * -1
    i = b * b - 4 * a * c
    if i < 0:
        return "no"
    elif i == 0:
        return "equal"
    else:
        x = math.sqrt(i)
        y = b - x
        
        z = y / (2 * a)
        return z
def getQuadra2(a, b, c):
    a = float(a)
    if a == 0:
        return "0"
    b = float(b)
    c = float(c)
    b = b * -1
    i = b * b - 4 * a * c
    
    x = math.sqrt(i)
    y = b + x
    
    z = y / (2 * a)
    return z

def digitCheck(x):
    try:
        x = float(x)
        return True
    except:
        return False

while(True):
    
    a = input("Please enter a: ")
    while digitCheck(a) == False:
        a = input("The input is not a number please enter again: ")
    while a == "0":
        a = input("a cannot be zero please enter again: ")
    b = input("please enter b: ")
    while digitCheck(b) == False:
        b = input("The input is not a number please enter again: ")
    
    c = input("please enter c: ")
    while digitCheck(c) == False:
        c = input("The input is not a number please enter again: ")
    if getQuadra(a, b, c) == "no":
        print("there is no answer for these numbers")
    elif getQuadra(a, b, c) == "equal":
        print("Both quadratic of numbers given above is 0")
        
    else:
        print("The first quadratic of numbers given above is : ", getQuadra(a, b, c))
        print("The second quadratic of numbers given above is : ", getQuadra2(a, b, c))

    enter_again = input("Would you like to test another set of numbers? (y/n) ")
    print("\n")
    if (enter_again != "y"):
        break
