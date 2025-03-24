print("Welcome to Mortgage Calculator")
try:
    salary = int(input("Enter your salary: "))
except:
    print("Invalid input")
    print("Please enter a valid number")
try:
    salary = int(input("Enter your salary: "))
except ValueError:
    print("Invalid input")
    print("Please enter a valid number")
else:
    if salary > 20000:
      print("You are eligible for a home loan")
    
    else:
      print("Sorry you are not eligible for a home loan")
finally:
    print("Thank you for using our home loan calculator")
    