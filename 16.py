#Write a program in python that counts the frequency of each character in a string.

str1 = input("Enter a string: ")

dict1 = {}

for i in range(0, len(str1)):
    if (str1[i] in dict1) == True:
        dict1[str1[i]] = dict1[str1[i]]+1
    else:
        dict1[str1[i]] = 1 
print(dict1)    

