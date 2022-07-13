import random
from time import time

start = time()

TARGET_NUMBER = random.randint(0, 100)

TOO_HIGH = ["You're guess is wayyy too far from the answer",   "Your guess is too high", "You're a bit too high", "You're a tiny bit too high", "You are so close"]

TOO_LOW = ["You're guess is wayyy too far from the answer", "Your guess is too low", "You're a bit too low", "You're a tiny bit too low", "You are so close"]

PERFECT = ("Good job! You have found the number, try again to  beat your time.\nYour time = {:.2f} seconds")


def program():
    while True:
        print(TARGET_NUMBER)
        user_input = input("Try guessing the number!\n")
        if not user_input.isdigit() or not 0 <= int(user_input) < 100:
            print("Please enter a whole number between 0 and 99.")
            continue
        guess = int(user_input)
        if guess > TARGET_NUMBER:
            if guess > TARGET_NUMBER + 5:
                print(TOO_HIGH[4])
            elif guess > TARGET_NUMBER + 10:
                print(TOO_HIGH[3])
            elif guess > TARGET_NUMBER + 15:
                print(TOO_HIGH[2])
            elif guess > TARGET_NUMBER + 35:
                print(TOO_HIGH[1])
            else:
                print(TOO_HIGH[0])
        elif guess < TARGET_NUMBER:
            if guess < TARGET_NUMBER - 5:
                print(TOO_LOW[3])
            elif guess < TARGET_NUMBER - 10:
                print(TOO_LOW[2])
            elif guess < TARGET_NUMBER - 15:
                print(TOO_LOW[1])
            elif guess < TARGET_NUMBER - 35:
                print(TOO_LOW[0])
            else:
                print(TOO_LOW[4])

        elif guess == TARGET_NUMBER:
            print(PERFECT.format(time()-start))
            break


program()
