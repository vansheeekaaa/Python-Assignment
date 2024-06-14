#Write a python program that takes a string as input and returns its length.

def length(str1):
    res = len(str1)
    return res


str1 = input("Enter a string: ")
res = length(str1)
print("Length of the string entered: ", res)