from random import randint


# function generates a random number between 1 - 100 and returns it to the primary function
def generate_random_number(min_num, max_num):
    ran_num = randint(min_num, max_num)
    return ran_num

# function checks generated random number against user's guess
def check_guess(random_num, user_guess):
    if random_num == user_guess:
        correct = True
    else:
        correct = False

    return correct


# if the guess is incorrect, provide a hint - if the user has guessed > 2 times, provide an additional hint
def hint(random_num, user_guess, guess):  
    rand_hint = randint(1,3)
    if guess > 2 and rand_hint == 1:    
        if random_num % 2 == 0:
            print("Hint: The number is even.")    
        else:
            print("Hint: The number is odd.")
    elif guess > 2 and rand_hint ==2:
        if random_num % 5 == 0:
            print("Hint: The number is a multiple of 5.")
        else: 
            print("Hint: The number is not a multiple of 5.")
    elif guess > 2 and rand_hint ==3:
        if random_num**2 < 1000:
            print("Hint: The number squared is less than 1,000.")
        else:
            print("Hint: The number squared is greater than 1,000.")
            
    if random_num < user_guess:
        print("Hint: Try a lower number.")
    else:
        print("Hint: Try a higher number.")

def main():
    min_num = 1
    max_num = 100
    correct = False
    guess = 0

    # welcome user and proviede a brief overview of the game
    print("Welcome to the Number Guessing Game!")
    print(f"I am thinking of a number between {min_num } and {max_num}. Try to guess my number!")
    random_num = generate_random_number(min_num, max_num)

    # loop through the game until the user guesses correct
    while correct is False:
        try:
            guess += 1
            user_guess = int(input("Please enter a number: "))
            if user_guess < min_num or user_guess > max_num:
                raise ValueError
        except ValueError:
            print(f"Invalid Entry! Please enter a valid number between {min_num} and {max_num}")
            continue

        # check if the guess matches the random number
        correct = check_guess(random_num, user_guess)

        # if the guess is incorrect, provide a hint
        if correct is False:
            hint(random_num, user_guess, guess)

    # if the guess is correct, display the random number and number of guesses
    print(f"Correct! You guessed my number {random_num} in {guess} attempts.")


if __name__ == "__main__":
    main()