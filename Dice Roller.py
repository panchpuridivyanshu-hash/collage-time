#Dice Roller – Simulates rolling dice and displays the result
import random

def roller():
    display=random.randint(1,6)
    print(f"You rolled a {display}!")


roller()    