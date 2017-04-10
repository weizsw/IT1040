import re
def getLength(user_string):
    return 1 + getLength(user_string[1:]) if user_string else 0

def getFirstIndex(user_string):
    return user_string[0]

def getLastIndex(user_string):
    size = getLength(user_string)
    LastIndex = size - 1
    return user_string[LastIndex]

def emailCheck(user_string):
    stringCheck = "email"
    result = 0
    for i in user_string:
        if stringCheck in user_string:
            result = "yes"
            break
        else:
            result = "no"

    return result

def alphaCheck(user_string):
    result = 0
    if (any(i.isalpha() for i in user_string)
        and any(i.isspace() for i in user_string)
        and all(i.isalpha() or i.isspace() for i in user_string)):
        result = "yes"
    else:
        result = "no"
    return result

def alphaAndDightsCheck(user_string):
    if digitsCheck(user_string) == "yes":
            return "no"
    if(all(i.isalpha() for i in user_string)):
        return "no"
    if re.match("^[A-Za-z0-9]*$", user_string):
    	return "yes"
    else:
    	return "no"
def digitsCheck(user_string):
    result = 0
    for i in user_string:
        if i not in "1234567890":
            result = "no"
            break
        else:
            result = "yes"
    return result

def lowerCheck(user_string):
    result = 0
    for i in user_string:
        if i not in "qwertyuiopasdfghjklzxcvbnm":
            result = "no"
        else:
            if user_string.islower() == True:
                result = "yes"
    return result

def upperCheck(user_string):
    result = "no"
    if all(i.isupper() for i in user_string):
        result = "yes"
    return result

while (True):



    try:
        
        user_string = input("Enter a string: ")
        
      

    except Exception as err:
        print ('An error occurred reading', user_string)
        print ('The error is', err)
        

    else:
        if not user_string:
           print("You did not enter anything!")
           break
        print("Length:", getLength(user_string))
        print("First character:", getFirstIndex(user_string))
        print("Last character:", getLastIndex(user_string))
        print("Contains email:", emailCheck(user_string))
        print("Only alphabetic letters and spaces:", alphaCheck(user_string))
        print("Only alphabetic letters and numbers:", alphaAndDightsCheck(user_string))
        print("Only numeric digits:", digitsCheck(user_string))
        print("All lower case:", lowerCheck(user_string))
        print("All upper case:", upperCheck(user_string))
        enter_again = input("Would you like to test another string? (y/n) ")
        print("\n")
        if (enter_again != "y"):
            break


