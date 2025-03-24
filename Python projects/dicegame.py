# Description: This file is used to test the code for the dice game.
#Dice game code
import random
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2   
def main():
    die1, die2 = roll_dice()
    print("You rolled a", die1, "and a", die2, "for a total of", die1 + die2)
    if die1 + die2 == 7 or die1 + die2 == 11:
        print("You win!")
    elif die1 + die2 == 2 or die1 + die2 == 3 or die1 + die2 == 12:
        print("You lose!")
    else: 
        print("The point is", die1 + die2)
        point = die1 + die2
        die1, die2 = roll_dice()
        while die1 + die2 != 7 and die1 + die2 != point:
            die1, die2 = roll_dice()
        if die1 + die2 == 7:
            print("You lose!")
        else:
            print("You win!")
main()
#Test code