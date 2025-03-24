print("Welcome to home loan calculator")
salary = int(input("What is your salary? "))

if salary > 20000:
    print("You are eligible for a home loan")
    credit_score = int(input("What is your credit score? "))
    if credit_score > 800:
        print("interest rate: 4%")
    elif credit_score > 780:
        print("Interest rate: 6%")
    else:
        print("interest rate: 9%")
else:
    print("Sorry you are not eligible for a home loan")