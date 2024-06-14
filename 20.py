#Write a python program that takes a list of numbers and returns their sum.
def sumOfAll(list1):
    ans = 0
    for i in list1:
        ans = ans+int(i)
    return ans

numbers = input("Enter numbers and leave spaces: ")
list1 = numbers.split()

summation = sumOfAll(list1)
print("Sum of all the numbers: ", summation)
