import random


def play_game():
    print("Welcome to the Number Guessing Game!")
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            attempts += 1

            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    play_game()
