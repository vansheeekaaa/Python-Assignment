"""Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result."""

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
op = input("Operation (+, -, /, *): ")

if op == '+':
    print("Sum: ", num1+num2)
elif op == '-':
    print("Difference: ", num1-num2)
elif op == '/':
    print("Division: ", num1/num2 )
elif op == '*':
    print("Multiplication: ", num1*num2)
else: 
    print("Symbol not recognised")    