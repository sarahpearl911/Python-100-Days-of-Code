import os
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

def clear_console():
  return os.system("clear")


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guessed_letters = ""

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear_console()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        if guess in guessed_letters:
            print(f"{guess} has already been guessed, please try again!")
        else:
          lives -= 1
          guessed_letters += guess
          print(f"{guess} is not in the word, you now have {lives} lives left.")
          if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The answer was {chosen_word}.")

    #Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
