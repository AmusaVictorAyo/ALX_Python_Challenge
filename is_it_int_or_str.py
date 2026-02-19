"""

ALX SE Python Project: Is it an Integer or a String?
This script intends to prompts the user to enter a value and determines whether it is an integer or a string using a match-case statement.
Author: [ALX SE]
Debugger: [Amusa Victor * ChatGPT]
Code:

value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")

I'm debbuging the code, check below.

"""


value = input("Enter a value (number or string): ")

try:
    value = int(value)
except ValueError:
   ...

match value:
    case int(): #If the value is an integer, it will match this case and print the corresponding message.
        print("You entered an integer:", value) 
    case str(): #If the value is a string, it will match this case and print the corresponding message.
        print("You entered a string:", value)
    case _: #If the value does not match either of the above cases, it will match this case and print the corresponding message.
        print("Invalid data type entered.")

print("Debugging complete. The code is now working as expected.\n")
# print(__doc__) - If ran, it will print the docstring at the beginning of the file, which contains the description and author information.