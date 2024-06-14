# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

str1 = input("Enter any string: ")
newString = ""

for char in str1:
    if (char not in punctuation) == True:
        newString = newString + char #string concatenation

print("Original string: ", str1)
print("Without punctuation: ", newString)
