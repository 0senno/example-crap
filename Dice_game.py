import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    return total

def main():
    print("Welcome to the Dice Rolling Game!")
    print("You will roll two dice and try to guess the total value.")
    while True:
        guess = input("Enter your guess (2-12): ")
        try:
            guess = int(guess)
            if 2 <= guess <= 12:
                break
            else:
                print("Invalid guess. Please enter a number between 2 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Rolling the dice...")
    total = roll_dice()
    print("The dice show:", total)

    if guess == total:
        print("Congratulations! You guessed the correct total.")
    else:
        print("Sorry, you guessed incorrectly. Better luck next time!")

if __name__ == "__main__":
    main()
