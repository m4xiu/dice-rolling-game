# This program simulates rolling a pair of dice.
# Loop
# Ask: roll the dice?
# If user say y 
#    generate two random numbers between 1 and 6
#    print then 
# If user say n
#    print thank you message
#    Terminate 
# Else 
#    print invalid choice

import random

while True:
    choice = input("🎲 Roll the dice? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled: {die1} and {die2}")
    elif choice == 'n':
        print("Thank you for playing! 🎲")
        break
    else:
        print("Invalid choice! Please enter 'y' or 'n'.")
