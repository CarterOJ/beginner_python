import random

def main():
    while True:
        magic_number = random.randint(1, 100)
        guess = input("I am thinking of a number 1-100. Take a guess or type 'Q' to quit: ")
        while True: 
            trimmed = guess.strip() 
            if trimmed.lower() == "q":
                print("Exiting guessing game")
                return
            elif " " in trimmed:
                guess = input("Can only accept one argument at a time! Guess again: ")
            elif not trimmed.isdigit():
                guess = input("Input must be an integer! Guess again: ")
            else:
                num_guess = int(guess)
                if num_guess < 1 or num_guess > 100:
                    guess = input("The magic number is between 1 & 100! Guess again: ")
                elif magic_number != num_guess:
                    guess = input("Not quite! Guess again: ")
                else:
                    print("You got it! Let's play again.")
                    break

if __name__ == "__main__":
    main()