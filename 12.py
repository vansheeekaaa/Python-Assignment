#Write a python program that calculates the sum of the digits of a given number.

num = int(input("Enter a number: "))

sum = 0
while num>0:
    dig = num%10
    sum+=dig
    num = int(num/10)

print("Sum of digits of", sum)    