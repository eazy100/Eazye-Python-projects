#odd and even numbers
def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
print(odd_even(num))
# This program will prompt the user to enter a number and then check if the number is odd or even.