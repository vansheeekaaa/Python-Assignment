#Write a python program that checks whether a given number is even or odd.

num = int(input("Enter a number: "))

if num & 1:
    print("The number is odd")
else:
    print("The number is even")