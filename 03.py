#Write a python program that calculates the factorial of a given number.

num = int(input("Enter a number: "))

factorial =1

for i in range (1, num+1):
    factorial = factorial*i

print("Factorial of {} is".format(num), factorial)
