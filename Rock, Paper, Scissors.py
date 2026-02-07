#Rock, Paper, Scissors – A simple game where the user plays against the computer
import random

def play_game():
    opetion=['rock', 'paper', 'scissors']

    computer_choice=random.choice(opetion)
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in opetion:
        print("Invalid choice!! please choose Rock, Paper,or Scissors  ")
        return

    print(f"your choice: {user_choice}")
    print(f"computer choice: {computer_choice}")

    if user_choice==computer_choice:
        print("it'a tie!!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")    


play_game()