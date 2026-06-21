# Rock Paper Scissors Game

import random

print("=" * 50)
print("ROCK PAPER SCISSORS GAME")

user_score = 0
computer_score = 0

ch = 'y'

while ch.lower() == 'y':

    print("=" * 50)
    print("Choose Your Move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("=" * 50)

    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("\nInvalid Choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("\n" + "=" * 50)
    print(f"You Chose      : {user_choice}")
    print(f"Computer Chose : {computer_choice}")
    print("=" * 50)

    # Game Logic
    if user_choice == computer_choice:
        print("Result : It's a Tie!")

    elif ((user_choice == "rock" and computer_choice == "scissors") or
          (user_choice == "paper" and computer_choice == "rock") or
          (user_choice == "scissors" and computer_choice == "paper")):

        print("Result : You Win!")
        user_score += 1

    else:
        print("Result : Computer Wins!")
        computer_score += 1

    print("\n" + "=" * 50)
    print("SCORE BOARD")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print("=" * 50)

    ch = input("Do you want to play again? (y/n): ")

    if ch.lower() == 'n':
        print("\n" + "=" * 50)
        print("THANK YOU FOR PLAYING!")
        print("=" * 50)
        print("Final Score")
        print(f"Your Score     : {user_score}")
        print(f"Computer Score : {computer_score}")
        print("=" * 50)
        break
