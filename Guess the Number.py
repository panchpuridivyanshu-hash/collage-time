#Guess the Number – The program randomly selects a number, and the user has to guess it
import random
def guess_number():
    print("wlecome to the Guess the Number Game!!")
    
    
    secret_number = random.randint(1, 100)
    attemps=0

    while True:
        guess=int(input("guess the number 1 to 100:"))
        attemps+=1
        if secret_number>guess:
            print("too low try again!!!")
        elif  secret_number<guess: 
            print("too high try again!!!")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attemps} attempts.")    
            break
guess_number()            