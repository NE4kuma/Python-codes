import random

print("Guess the number")

def guess(x):
    random_number = random.randint(1, x)                                #imporant creat a number between 1 and 'x'
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:  "))      
        if guess > random_number:
            print("The namber is smaller!")
        elif guess < random_number:
            print("The namber is bigger!")
        
    print(f"Nice, you got the number, the number was {random_number}")  #if the number getting guessed, the loop going to finsh, 
        
guess(100)                                                              #set the 'x'

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            high = guess + 1
    
    print(f"The computer has guessed ur number, guess number was {guess}")

computer_guess(10)
