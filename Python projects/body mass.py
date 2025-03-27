# This program calculates the body mass index of a person and tells them if they are underweight, normal, overweight or obese.
height =  float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
BMI = round(weight / height**2,2)   

if BMI < 18.5:
    print(f"Your BMI is {BMI} , you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI} ,  your weight is normal")
elif BMI < 30:
    print(f"Your BMI is {BMI} , you are overweight")
else:
    print(f"Your BMI is {BMI} , You are obese")
