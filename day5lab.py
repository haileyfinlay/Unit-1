def apt_search1(city,max_rent,min_beds,pets_allowed = False):
    if pets_allowed:
        print(f"Welcome to GC Property Management!\nLooking up listings in {city} for {min_beds} bedroom apartments that allow pets,\nall within a budget of {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management!\nLooking up listings in {city} for {min_beds} bedroom apartments,\nall within a budget of {max_rent} per month...")
apt_search1("Charlotte",2000,2,True)

def apt_search2(city,max_rent,min_beds = 2,pets_allowed = False):
    if pets_allowed:
        print(f"Welcome to GC Property Management!\nLooking up listings in {city} for {min_beds} bedroom apartments that allow pets,\nall within a budget of {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management!\nLooking up listings in {city} for {min_beds} bedroom apartments,\nall within a budget of {max_rent} per month...")

apt_search2("Charlotte",4000)
apt_search2("Charlotte",4000,5)
apt_search2("Charlotte",4000,pets_allowed= True)

add_100 = lambda x: x+100
print(add_100(4))
square = lambda x: x*x
print(square(5))
conc = lambda x: "- "+ x
print(conc("Hello"))
div = lambda x: x/3
print(div(12))