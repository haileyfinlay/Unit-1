welc = input('Hello! What is your name? ')
user_int = input('Enter an integer between 1 and 100, '+welc+': ')
#print(user_int)
#user_int = int(user_int)
x = int(user_int) % 2
#print(x)
while int(user_int) not in range (1,100):
    user_int = (input('Enter an integer between 1 and 100, ' + welc + ': '))
    x = int(user_int) % 2

if x == 1 and int(user_int) < 60:
    print(user_int + " is odd and less than 60")
elif x == 0 and (2 <= int(user_int) <= 24):
    print(user_int + " is even and less than 25")
elif x == 0 and (26 <= int(user_int) <= 60):
    print(user_int + " is even and between 26 and 60 inclusive")
elif x == 0 and int(user_int) > 60:
    print(user_int + " is even and greater than 60")
elif x == 1 and int(user_int) > 60:
    print(user_int + " is odd and greater than 60")

while True:
    response = input("Would you like to enter another integer between 1 and 100, " + welc + "? (y/n) ")
    if response == "y":
        nxt = input("Okay, great! Enter your next integer here: ")
        nxt = int(nxt)
        while nxt not in range(1, 100):
            nxt = int((input('Enter an integer between 1 and 100, ' + welc + ': ')))
        x = nxt % 2
        if x == 1 and nxt < 60:
            print(str(nxt) + " " + "is odd and less than 60")
        elif x == 0 and (2 <= nxt <= 24):
            print(str(nxt) + " " + "is even and less than 25")
        elif x == 0 and (26 <= nxt <= 60):
            print(str(nxt) + " " + "is even and between 26 and 60 inclusive")
        elif x == 0 and nxt > 60:
            print(str(nxt) + " " + "is even and greater than 60")
        elif x == 1 and nxt > 60:
            print(str(nxt) + " " + "is odd and greater than 60")
    if response == "n":
        print("Hope you learned a lot! Tata for now, " + welc + "!")
        break

#welc = input('Hello! What is your name? ')
#user_int = input('Welcome ' + welc + '! Enter an integer between 1 and 100: ')
#while user_int not in range(1,100):
  #  print("wrong. try again")
  #  user_int = input("Try again here: ")
  #  break