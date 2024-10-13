import random

print("The computer have to guess our number!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''                               #erstellt 3 Variablen
    while feedback != 'c':                      
        if low != high:
            guess = random.randint(low, high)   #erstellt eine Zufällige Zahl, von low und high(x)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            high = guess + 1
    
    print(f"The computer has guessed ur number, guess number was {guess}")

computer_guess(10)                              # festlegung der Range, von low bis hig