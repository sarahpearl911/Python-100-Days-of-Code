#i first made this game in the way that was easiest to me
#however, this is part of a lesson about local and global variables
#so we were expected to define functions to get practice with these variables
#once again, i decided to go back and rewrite everything according to the intention of the lesson
#this is good practice for me to get used to using functions and having less repetitive code

# import random

# print("Welcome to the number guessing game!")
# print("I'm thinking of a number between 1 and 100.")
# level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# answer = random.randint(1, 100)

# attempts = 0

# if level == "easy":
#   attempts = 10
# elif level == "hard":
#   attempts = 5

# print(f"You have {attempts} attempts to guess the number.")

# def decrease_attempts():
#   return attempts - 1
  
# while attempts > 0:
#   guess = int(input("Make a guess: "))
#   if guess > answer:
#     attempts = decrease_attempts()
#     print("Too high.")
#   elif guess < answer:
#     attempts = decrease_attempts()
#     print("Too low.")
#   elif guess == answer:
#     print("You win!!!")
#     attempts = 0
#   if attempts > 0 and guess != answer:
#     print(f"You have {attempts} guesses left.")
# if attempts == 0 and guess != answer:
#   print(f"You lose! The answer was {answer}.")



import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

answer = random.randint(1, 100)

level_easy = 10
level_hard = 5

def check_guess(guess, answer):
  if guess < answer:
    print("Too low.")
  elif guess > answer:
    print("Too high.")
  else:
    print("That's the answer! You win!")

def set_level():
  if level == "easy":
    return level_easy
  elif level == "hard":
    return level_hard

def end_game(chances, guess, answer):
  if chances == 0 and guess != answer:
    print(f"You lose! The number was {answer}.") 

def game():
  chances = set_level()
  guess = 0
  while guess != answer and chances > 0:
    print(f"You have {chances} guesses left.")
    guess = int(input("Guess a number: "))
    check_guess(guess, answer)
    chances -= 1
  end_game(chances, guess, answer)


game()
