#Burger calculator
print("Welcome to EAZY Burgers")
print("Here is our menu:")
print("Medium: R20")
print("Normal: R25")
print("Large: R30")
size = input("What size would you like? (M, N, L) ")
add_mushrooms = input("Do you want extra mushrooms? (Y/N) ")
add_cheese = input("Do you want extra cheese? (Y/N) ")

bill = 0
if size == "M":
    bill += 20
elif size == "N":
    bill += 25
elif size == "L":
    bill += 30

if add_mushrooms == "Y":
    if size == "L":
        bill += 5
    else:
        bill += 2
if add_cheese == "Y":
    bill += 5
print(f"Your final bill is: R{bill}")
