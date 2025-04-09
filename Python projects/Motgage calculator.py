print("Welcome to Mortgage Calculator")
salary = int(input("What is your salary? "))

if salary > 20000:
    print("You are eligible for a mortgage")
elif salary == 15000:
    print("Your application has been send to Credit vetting!")
else:
    print("Sorry you need additional funds for a mortgage")

    if salary <10000:
        print("Sorry you are not eligible for a mortgage")
    else:
        print("Your Application has been declined!")