#Addition
def addition(a:int, b:int):
    return a + b


#Subtraction
def subtraction(a:int, b:int):
    return a - b


#Division
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return 'Cannot divide by zero'