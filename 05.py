#Write a program that takes a string input from the user and writes it to a text file.

str1 = input("What would you like to write in your file? ")
myFile = open('/home/vanshika/Desktop/217_Vanshika_Python assignment1/05 text file.txt', 'w')
print(str1, file = myFile)