import random
from game_data import data
from art import logo
from art import vs
import os

def clear_console():
  return os.system("clear")

#data list is ordered as name, follower_count, description, country

person_a = random.choice(data)
person_b = random.choice(data)

answer = "d"
guess = "c"
score = 0
game = True


while game:
  print(logo)
  if guess == answer:
    print(f"That's correct! Your score is: {score}")
  print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
  print(vs)
  print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
  if person_a["follower_count"] > person_b["follower_count"]:
    answer = "a"
  elif person_a["follower_count"] < person_b["follower_count"]:
    answer = "b"
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  if guess == answer:
    score += 1
    person_a = person_b
    person_b = random.choice(data)
    clear_console()
  elif guess != answer:
    game = False
    clear_console()
    print("You lose!")
