import random
def guess(x):
    random_numb = random.randint(1, x)
    guess = 0
    try:
        while guess != random_numb:
            guess = int(input(f"Enter a number between 1 and {x}: "))
            if guess < random_numb:
                print("Sorry the number you've guess is low")
            elif guess > random_numb:
                print("Sorry the number you've guessed is high")
        print("Wonderful! You've guessed the correct number")
    except Exception as e:
        print(e)
guess(10)
