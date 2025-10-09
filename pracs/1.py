import random

def guessing_game():
    print("welcome to the number guessing event")
    print("guees the no. btw 1 to 100")

    secret_no=random.randint(1,100)
    attempts=0

    while True:
        try:
            guess=int(input("enter your choice :"))
            attempts += 1
            if guess < secret_no:
                print("too low")
            elif guess > secret_no:
                print("too high")
            else:
                print("congo u guessed it shi...")
            break
        except ValueError:
            print("enter valid bluddd")

guessing_game()