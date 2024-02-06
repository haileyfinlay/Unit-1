names = ["Jordan","Jenna","Emily"]
hometown = ["Yorktown, VA","Sillyville, CA","Tampa, FL"]
foods = ["sandwiches","burgers n fries","pizza"]

while True:
  while True:
    student_num = int(input("Which student would you like to learn about? Select student 1-3: "))
    position = student_num - 1
    if student_num > len(names):
      print("Only numbers 1-3 are valid. Please try again")
    else:
      break
  while True:
    choice = input(f"Student {student_num} is {names[position]}. What would you like to know about {names[position]}?\nEnter hometown or favorite food: ")
    if choice == "hometown":
      print(f"{names[position]}'s hometown is {hometown[position]}.")
      break
    elif choice == "favorite food":
      print(f"{names[position]}'s favorite food is {foods[position]}.")
      break
    else:
      print("That was an invalid response. Please try 'hometown' or 'favorite foods'.")
  again = input("Would you like to learn about another student? (y/n): ")
  if again == "n":
    print("Goodbye!")
    break