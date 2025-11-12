import random

jackpot = random.randint(1,100)

guess_num = int(input("Enter your guess number: "))
counter = 0

while guess_num != jackpot:
    if guess_num < jackpot:
        print("Wrong! please guess Higher")
    else:
        print("Wrong! please guess Lower")  
    
    guess_num = int(input("Enter your guess number: "))
    counter+=1
    
else:
    print("You choose the correct number after ",counter," count.")
