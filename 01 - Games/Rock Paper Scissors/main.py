import random

rock_0 = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_1 = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_2 = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Choose between Rock (0), Paper (1), or Scissors (2)
user_choice = input(
    "\nWhat do you choose? Type: \n0 for Rock \n1 for Paper \n2 for Scissors\n"
)

computer_choice = random.randint(0, 2)

# Print the user's choice
if not user_choice.isdigit():
    print("You've entered an invalid value, Game Over.\n")
elif int(user_choice) > 2:
    print("You've entered an invalid number, Game Over.\n")
else:
    user_choice = int(user_choice)
    if user_choice > 2:
        print(
            "You've entered an invalid number, try again and choose a number between 0-2."
        )
    elif user_choice == 0 or user_choice == 1 or user_choice == 2:
        if user_choice == 0:
            print(f"You chose: Rock {rock_0}")
        elif user_choice == 1:
            print(f"You chose: Paper {paper_1}")
        elif user_choice == 2:
            print(f"You chose: Scissors {scissors_2}")

    # Print the computer's choice & determine the winner
    # Computer chooses Rock - You lose, its a draw, you winS
    if computer_choice == 0:
        print(f"The computer chose: Rock {rock_0}")
        if user_choice == 2:
            print("You lose, Rock beats scissors.\n")
        elif user_choice == 0:
            print("It's a draw!\n")
        else:
            print("You Win!! Paper beats rock.\n")

    # Computer chooses Paper - You lose, its a draw, you win
    if computer_choice == 1:
        print(f"The computer chose: Paper {paper_1}")
        if user_choice == 0:
            print("You lose, Paper beats rock.\n")
        elif user_choice == 1:
            print("It's a draw!\n")
        else:
            print("You win!! Scissors beats paper.\n")

    # Computer chooses Scissors - You lose, its a draw, you win
    if computer_choice == 2:
        print(f"The computer chose: Scissors {scissors_2}")
        if user_choice == 1:
            print("You lose, Scissors beats paper.\n")
        elif user_choice == 2:
            print("It's a draw!\n")
        else:
            print("You win!! Rock beats paper.\n")
