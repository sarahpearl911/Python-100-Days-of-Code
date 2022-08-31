rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
print("Let's play rock paper scissors!")
you_choose = input("Choose one- type 1 for rock, 2 for paper, or 3 for scissors\n")
you_choose_int = int(you_choose)
if you_choose_int == 1:
  print(rock)
elif you_choose_int == 2:
  print(paper)
elif you_choose_int == 3:
  print(scissors)

rps = [1, 2, 3]
comp_choice = random.choice(rps)
print("The computer chose:\n")
if comp_choice == 1:
  print(rock)
elif comp_choice == 2:
  print(paper)
elif comp_choice == 3:
  print(scissors)

if you_choose_int == comp_choice:
  print("It's a tie!")
elif you_choose_int == 1 and comp_choice == 2:
  print("You lose!")
elif you_choose_int == 1 and comp_choice == 3:
  print("You win!")
elif you_choose_int == 2 and comp_choice == 3:
  print ("You lose!")
elif you_choose_int == 2 and comp_choice == 1:
  print("You win!")
elif you_choose_int == 3 and comp_choice == 1:
  print("You lose!")
elif you_choose_int == 3 and comp_choice == 2:
  print("You win!")
else:
  print("You made an invalid choice! Read the rules and try again!")
