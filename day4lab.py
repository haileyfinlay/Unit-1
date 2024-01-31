# Define Function
def heating_cooling(actual_temp, desired_temp):
    if actual_temp == desired_temp:
        print("Standby")
    elif actual_temp < desired_temp:
        print("Run heat")
    elif actual_temp > desired_temp:
        print("Run A/C")

# Test Function
heating_cooling(70,72)
heating_cooling(72,64)
heating_cooling(70,70)

# User Inputs with Function
act = int(input("What is the current temperature?: "))
des = int(input("What is your desired temperature?: "))
heating_cooling(act,des)

# Extended Challenge
def convert_temp(temp_celsius, target_unit):
    if target_unit == 'K':
        temp_celsius = temp_celsius + 273.15
    elif target_unit == 'F':
        temp_celsius = (temp_celsius * (9/5) + 32)
    elif target_unit == 'C':
        temp_celsius
    print(f"{temp_celsius} degrees {target_unit}")

convert_temp(0, 'K')
convert_temp(0, 'F')



