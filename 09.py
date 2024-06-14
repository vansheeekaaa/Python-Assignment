#Write a python program that checks if a substring is present in a given string
str1 = input("Enter a string: ")
str2 = input("Subsstring you want to search for: ")

if (str2 in str1) == True: 
    print("Yes! {} is present in {}".format(str2, str1))
else:
    print("No! {} is not present in {}".format(str2, str1))