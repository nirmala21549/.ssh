number = 10
max_guesses = 3
guess_count = 0

print("I'm thinking of a number...")

while guess_count < max_guesses:
    guess = input("What number am I thinking of? (Enter 'q' to quit) ")

    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print("Too high! Try again.")
    elif int(guess) < number:
        print("Too low! Try again.")
    
    guess_count += 1

if guess_count == max_guesses:
    print("Sorry, you've reached the maximum number of guesses.")
