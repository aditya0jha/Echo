import random
def guess(x):
    low = 1
    high = x
    feedback = ''
    try:
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            feedback = input(f"Please tell me wheather \'{guess}\' is Too High or Too Low by pressing (h) and (l) respectively. If the number is correct then press (c).")
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        print("Wonderful! I've guessed the right number!!")
    except Exception as e:
        print(e)
guess(100)


