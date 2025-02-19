import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("=====================================")
    print("Instructions:")
    print("1. I'm thinking of a number between 1 and 100.")
    print("2. Your goal is to guess the number.")
    print("3. I will tell you if your guess is too high or too low.")
    print("4. Keep guessing until you get it right.")
    print("=====================================")
    
    while True:
        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed_correctly = False

        print("\nI have selected a number. Try to guess it!")

        # Loop until the player guesses correctly
        while not guessed_correctly:
            try:
                # Prompt the user for a guess
                guess = input("\nEnter your guess (1-100): ")

                # Ensure the input is a valid number
                if not guess.isdigit():
                    print("Oops! That's not a valid number. Please enter a number between 1 and 100.")
                    continue
                
                guess = int(guess)
                
                if guess < 1 or guess > 100:
                    print("Please guess a number between 1 and 100.")
                    continue

                attempts += 1

                # Check if the guess is too low, too high, or correct
                if guess < number_to_guess:
                    print("Your guess is too low. Try again!")
                elif guess > number_to_guess:
                    print("Your guess is too high. Try again!")
                else:
                    guessed_correctly = True
                    print(f"\nCongratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            
            except ValueError:
                print("Oops! Something went wrong. Please enter a valid number.")
        
        # Ask if the user wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    number_guessing_game()
