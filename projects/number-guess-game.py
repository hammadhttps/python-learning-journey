import random

print("Welcome to the Number Guess Game!")

random_number = random.randint(1, 100)  

attempts = 0

while attempts < 5:
    guess = int(input(f"Enter your guess:The number is between {random_number-10} and {random_number + 10}: "))
    if guess == random_number:
        print("You guessed the number!")
        break
    elif guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    print("Try again!")
    print("You have 5 attempts to guess the number.")
    print("You have", 5 - attempts, "attempts left.")
    attempts += 1
    print("--------------------------------")
print("You have run out of attempts. The number was", random_number)





