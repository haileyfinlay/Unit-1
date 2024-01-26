print("Learn your squares and cubes!")
user_int = int(input("Enter an integer: "))
print("Number  Squared  Cubed")
print("======  "+"=======  "+"=====")
for x in range(0,user_int+1):
    print(f'{f"{x}":<8}{f"{x**2}":<9}{f"{x**3}"}')
    #print(f"{x}       {x**2}        {x**3}")
cont = input("Continue? (y/n): ")
while cont == 'y':
    user_int = int(input("Enter an integer: "))
    print("Number  Squared  Cubed")
    print("======  " + "=======  " + "=====")
    for x in range(1, user_int + 1):
        print(f'{f"{x}":<8}{f"{x ** 2}":<9}{f"{x ** 3}"}')
    cont = input("Continue? (y/n): ")
print("That was fun! Goodbye now.")

## Extra tricks to consider:
#print("f", end=" ")
#print("r", end=" ")
#print("f", end="\t")
#print("r", end="\n")
# \t tab
# \n