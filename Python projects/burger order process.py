#Burger order program
Mini = ("Mini Burger", 10)
Normal = ("Normal Burger", 15)
Large = ("Large Burger", 20)
ExtraCheesextraCheese = ("Extra Cheese", 5)
ExtraMarshrooms = ("Extra Marshrooms", 10)
print("Welcome to Burger Palace")   
print("Here is our menu")
print(f"{Mini[0]}: R{Mini[1]}")
print(f"{Normal[0]}: R{Normal[1]}")
print(f"{Large[0]}: R{Large[1]}")
size = input("What size would you like? (M, N, L) ")
if size == "M":
    print(f"Your order is {Mini[0]}: R{Mini[1]}")
elif size == "N":
    print(f"Your order is {Normal[0]}: R{Normal[1]}")
elif size == "L":
    print(f"Your order is {Large[0]}: R{Large[1]}")
else:
       ExtraCheese = input("Do you want ExtraCheese?, (Y/N) ")
       ExtraMarshrooms = input("Do you want ExtraMarshrooms?, (Y/N) ")
if ExtraCheese == "Y":
        print("You have added extra cheese to your order  {extraCheese[R5]}: R{extraCheese[1]}")
if ExtraMarshrooms == "Y":
        print("You have added extra marshrooms to your order {extraMarshrooms[R10]}: R{extraMarshrooms[1]}")
else:
    print("You have not added extra cheese to your order")
    print("You have not added extra marshrooms to your order")
    print("Thank you for ordering from Burger Palace")
    print("Your order will be ready in 10 minutes")