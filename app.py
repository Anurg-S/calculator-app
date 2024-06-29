from calc_funct import addition, subtraction
from multiplication import multiplication
from area import calculate_area_rectangle

def calculator():
    print('Welcome to the Calculator App')
    print('''Please select the desired option
          
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Area
          ''')
    
    user_option = int(input('Enter the option '))

    a = int(input('Enter the first number '))
    b = int(input('Enter the second number '))

    if user_option == 1:
        result = addition(a,b)
    elif user_option == 2:
        result = subtraction(a,b)
    elif user_option == 3:
        result = multiplication(a,b)
    elif user_option == 4:
        result = calculate_area_rectangle(a,b)

    print('Result: ', result)
    
if __name__ == '__main__':
    calculator()