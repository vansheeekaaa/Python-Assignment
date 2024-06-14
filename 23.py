#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

strr = """Welcome User! You would like to convert
          1. Celsius to Fahrenheit
          2. Fahrenheit to Celsius
          Enter 1/2: """

choice = int(input(strr))

if choice==1:
    cel = float(input("Enter temp in Celsius: "))
    fht = cel * (9.0/5.0) + 32
    print("{}°C = {}F".format(cel, fht))

elif choice==2:
    fht = float(input("Enter temp in Fahrenheit: "))
    cel = (fht - 32) * 5.0/9.0
    print("{}F = {}°C".format(fht, cel))

else: 
    print("Not recognised!")   