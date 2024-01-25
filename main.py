first_name = "Fred"
print(first_name)
my_fist_var = 3

#1.1
string = input('Type something')
print(string)

#1.2
num = input("Enter a number:")
print(int(num)+1)

#1.3
num2 = float(input("Enter a number again:"))
print(num2 + 0.5)

#1.4
num3= float(input("another number plz:"))
num4=float(input("one more!:"))
num5 = num3+num4
print(num5)
# could also just have done this instead of assigning num5
print(num3+num4)

#1.5
num6= float(input("another number plz:"))
num7=float(input("one more!:"))
num8 = num6*num7
print(num8)
# could also have just done this
print(num6*num7)

#1.6
num9= int(input("another number now:"))
num10=int(input("one more!:"))
num11 = num9/num10
print(num11)
## Program fails when you try entering a decimal for num9 or num10!

##1.7
reply = input("Enter a boolean:")
if reply == "True":
    print("You entered: True" + "\nThe opposite of what you entered is: False")
elif reply == "False":
    print("You entered: False" + "\nThe opposite of what you entered is: True")

## another way
reply = bool(input("Enter a boolean part 2: "))
if reply == "True":
    print("You entered: True" + "\nThe opposite of what you entered is: False")
else:
    print("You entered: False" + "\nThe opposite of what you entered is: True")

## easiest way
user_input = bool(int(input("Enter 1 or 0:")))
print("You entered:", user_input)
print("The opposite of what you entered is:", not user_input)

## my other way explained
#Ask user for value
user_input = input("Enter a boolean last time:")
#right = True if literally typed True since the comparrison is correct
#If not True typed then it is false
right = user_input == "True"
#This sets a boolean only value based off of if True matched what was typed
right2 = bool(right)
#Prints the results
print("You entered:", right2)
print("The opposite of what you entered is:", not right2)

#another example
# Ask the user for input
user_input = input("Enter something (anything non-empty will be considered True): ")
# Convert the input to a boolean: non-empty is True, empty is False
input_bool = bool(user_input)
# Print the opposite
print("The opposite of what you entered is:", not input_bool)
