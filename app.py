from calc_funct import addition, subtraction

def calculator():
    print('Welcome to the Calculator App')
    print('''Please select the desired option
          
          1. Addition
          2. Subtraction
          ''')
    
    user_option = int(input('Enter the option '))

    a = int(input('Enter value of A '))
    b = int(input('Enter Value of B '))

    if user_option == 1:
        result = addition(a,b)
    elif user_option == 2:
        result = subtraction(a,b)

    print('Result: ', result)
    
if __name__ == '__main__':
    calculator()