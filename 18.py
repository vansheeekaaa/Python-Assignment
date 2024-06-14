#Write a python program that checks if two strings are anagrams of each other.
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
str1 = str1.lower()
str2 = str2.lower()
#I can use split and then see if equal
list1 = list(str1)
list1.sort()
list2 = list(str2)
list2.sort()

if list1==list2:
    print("Annagram")
else:
    print("Not Anagram")