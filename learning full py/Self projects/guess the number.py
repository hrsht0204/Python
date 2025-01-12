import random

# Set of possible numbers (strings)
PriSet = {"3", "4", "5", "6", "7", "8", "9", "10", "2", "1", "0"}
MainK = PriSet.pop()  # Randomly pop an element from the set
MainK2 = int(MainK)  # Convert it to an integer

# Reveal the correct answer for testing or curiosity
print(f"(DEBUG) The correct number is: {MainK2}")

index = 1
max_tries = 10
search = int(input(f"{index} Your Number guess is: "))

while index <= max_tries:
    if MainK2 == search:  # Correct guess
        Vsounds = ["Well done", "Is this your first try?", "You are so good!"]
        print(random.choice(Vsounds), search)
        break
    else:  # Incorrect guess
        DSounds = [
            "Good guess, try again!",
            "Nah, try harder.",
            "Very close, buddy.",
            "You should leave, JK!",
            "Shall I help? Of course not, be independent!",
        ]
        print(random.choice(DSounds))
        index += 1
        if index > max_tries:  # If out of tries after incrementing
            print(f"Out of tries! The correct number was {MainK2}.")
            break
        search = int(input(f"Your {index} Guess: "))
