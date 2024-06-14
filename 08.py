#Write a python program that concatenates two strings and returns the result.

def stringConcatinate(str1, str2):
    str3 = str1+str2
    return str3

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
result = stringConcatinate(str1, str2)
print("Concatenated String: ", result)
