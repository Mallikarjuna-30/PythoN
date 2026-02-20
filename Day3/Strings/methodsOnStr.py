text = "Hello World"

print(type(text))  # data tye => string
print(len(text))  # length of the string => 11
print(text.lower())  # turn text to lower case
print(text.upper())  # turn text to upper case
print(text.strip())  # remove extra white space from the string
print(text.replace("H", "J"))  # replace H with J
print(text.title())  # turn text to title case
print(text.split(" "))  # split text into list
# print(text.find("W"))  # find index of W
# print(text.count("l"))  # count number of l
# print(text.index("l"))  # find index of l
# print(text.isnumeric())  # check if text is numeric
# print(text.isalpha())  # check if text is alpha
# print(text.isalnum())  # check if text is alphanumeric
# print(text.isdecimal())  # check if text is decimal
# print(text.isprintable())  # check if text is printable
# print(text.isdigit())  # check if text is digit
print(text.startswith("Hello"))  # check if text starts with Hello
print(text.endswith("World"))  # check if text ends with World
# print(text.join(" "))  # join text with space
print(text[0:15:2])  # slicing
print(text[-1:-15:-1])
print(text[5:] * 5)
print(text + " Python Training")  # string concatenation
