#Write a python program that generates the first n numbers in the Fibonacci sequence.

number = int(input("Enter the number of terms you want to print in Fibonacci seq: "))

t1 = 1
t2 = 1

if number==1:
    print(t1)
elif number==2:
    print(t1, t2)
else:
    print(t1, t2, end = " ")
    for i in range(number-2):
        next = t1+t2
        print(next, end = " ")
        t1 = t2
        t2 = next