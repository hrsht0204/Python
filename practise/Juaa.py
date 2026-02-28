import random

Bal = 100
# The secret number is set only once
num = random.randint(1, 10)

print(f"Current Balance: {Bal}")

# Start a loop that lets the user guess multiple times
while True:
    guss_str = input("Guess the number: ")

    try:
        guss_int = int(guss_str)

        # 1. Check for the Secret Code (69)
        if guss_int == 69:
            print(f"*** Secret code activated!{num}. ***")
            
            continue 

        # 2. Check for the Correct Guess
        elif guss_int == num:
            print("You guessed it right! Congratulations!")
            Bal += 100
            print(f"New Balance: {Bal}")
            break # Exit the loop since the game is over
            
        # 3. Handle an Incorrect Guess
        else:
            print(f"Wrong guess, try again! (You guessed {guss_int})")
            Bal -= 50
            print(f"Balance after wrong guess: {Bal}")
            # The loop continues to the next guess

    # Handle non-numeric input error
    except ValueError:
        print("Invalid input. Please enter a number.")
        # The loop continues to the next guess

# Code after the loop finishes
print("Game Over. Thanks for playing!")