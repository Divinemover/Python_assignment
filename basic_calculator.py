first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
sign = input('Enter the operation sign (+ for addition, - for subtraction, * for multiplication, / for division): ')

if sign == '+':
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif sign == '-':
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif sign == '*':
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif sign == '/':
    if second_number == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
else:
    print("Invalid operation! Please enter one of the following: +, -, *, /")
