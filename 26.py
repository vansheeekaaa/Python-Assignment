#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix

str1 = input("Enter a string: ")
prefix = input("Prefix to check for: ")
suffix = input("Suffix to check for: ")

if str1.startswith(prefix) == True:
    print("Yes! String: ({}) start with ({})".format(str1, prefix))
else: 
    print("No! String: ({}) do not start with ({})".format(str1, prefix))

if str1.endswith(suffix) == True: 
    print("Yes! String: ({}) end with ({})".format(str1, suffix)) 
else: 
    print("No! String: ({}) do not end with ({})".format(str1, suffix))   