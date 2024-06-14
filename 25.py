#Write a program that copies the contents of one text file to another.
read = open('/home/vanshika/Desktop/217_Vanshika_Python assignment1/05 text file.txt', 'r')
write = open('/home/vanshika/Desktop/217_Vanshika_Python assignment1/25.txt', 'w')
print(read.read(), file=write)