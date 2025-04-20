from hangman_art import stages, logo2, logo3
from hangman_words import word_list
import random

# Game Intro and Setup
random_word = random.choice(word_list)
lives = 6
print(logo3+"\n")
placeholder = ""
for position in range(len(random_word)):
    placeholder += "_"

print(f"Guess this word: {placeholder}\n")

game_over = False
correct_letters = []

while not game_over:
    print(f"********************{lives}/6 LIVES LEFT********************")
    guess = input("Choose a letter:\n").lower()

    #Multiple Guess Confirmation
    if guess in correct_letters:
        print(f"\n~~~You've already guessed {guess} correctly!!~~~")

    # Display Revealed or Hidden Characters
    display = ""
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word: {display}")

    # LOSE LIFE CONDITION
    if guess not in random_word:
        lives -= 1
        print(f"\n~~~You guessed {guess}, that's not in the word. You lost a life~~~")

        # YOU LOSE CONDITION
        if lives == 0:
            game_over = True
            print(f"**************The correct word was: {random_word}! YOU LOSE**************")

    # YOU WIN CONDITION
    if "_" not in display:
        game_over = True
        print(f"********************YOU WIN!********************")
        print(logo2)

    print(stages[lives])