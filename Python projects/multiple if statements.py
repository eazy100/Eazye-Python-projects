print("Welcome to home loan calculator")
salary = int(input("What is your salary? "))
rate = 0

if salary > 20000:
    print("You are eligible for a home loan")
    credit_score = int(input("What is your credit score? "))
    if credit_score > 800:
        rate = 4
        print("interest rate: 4%")
    elif credit_score > 750:
        rate = 6
        print("Interest rate: 6%")
else:
    rate = 8
    print("Interest rate: 8%")
disability = input("Do you have a disability? ( Y or N) ")
if disability == "Y":
     rate = rate - 2
print("You are eligible for a 2% discount")
print(f"Final interest Rate: {rate}%")
if rate < 5:
    print("You are eligible for a home")
else:
    print("Sorry you are not eligible for a home loan")
