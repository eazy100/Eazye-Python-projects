print("Welcome to home loan calculator")
salary = int(input("What is your salary? "))

if salary > 20000:
    print("You are eligible for a home loan")
    credit_score = int(input("What is your credit score? "))
    if credit_score > 800:
        print("interest rate: 4%")
    else:
        print("Interest rate: 6%")
else:
    print("You are not eligible for a home loan")