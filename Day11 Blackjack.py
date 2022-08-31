import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_console():
  return os.system("clear")

def blackjack():
  print(logo)
  print("Welcome to Blackjack!")
  start = input("Type 'deal' when you're ready to start playing: ").lower()
  if start == "deal":
    player_hand = []
    for num in range(1, 3):
      player_hand.append(random.choice(cards))
    player_score = sum(player_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")
    comp_hand = []
    for num in range(1, 3):
      comp_hand.append(random.choice(cards))
    comp_score = sum(comp_hand)
    print(f"Computer's first card: {comp_hand[0]}")
    ace_comp = True
    while ace_comp:
      while comp_score < 17:
        comp_hand.append(random.choice(cards))
        comp_score = sum(comp_hand)
      if 11 in comp_hand and comp_score > 21:
        comp_hand.remove(11)
        comp_hand.append(1)
        comp_score = sum(comp_hand)
      else:
        ace_comp = False

        

    ace = True
    keep_dealing = True
    while keep_dealing:
      if player_score == 21 and comp_score != 21:
        keep_dealing = False
        print("You got a blackjack! You win!")
      elif player_score == 21 and comp_score == 21:
        keep_dealing = False
        print("Both you and the computer got blackjack! It's a tie!")
      else:
        while ace:
          if 11 in player_hand:
            print("You have an ace in your hand. Would you like it to count as 11 or 1?")
            ace_player = int(input("Enter '11' or '1': "))
            if ace_player == 1:
              player_hand.remove(11)
              player_hand.append(1)
              player_score = sum(player_hand)
              print(f"Your new score is {player_score}.")
              ace = False
              keep_dealing = True
            else:
              ace = False
          else:
            ace = False


        another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another == "y":
          new_card = random.choice(cards)
          player_hand.append(new_card)
          player_score = sum(player_hand)
          print(f"You pulled a {new_card}. Your hand is now {player_hand} and your score is {player_score}")


        if 11 in player_hand and player_score > 21:
          ace = True
        
          
        if 11 not in player_hand and player_score > 21:
          keep_dealing = False
          print("You went over 21. You lose!")
        elif another == "n":
          keep_dealing = False
          if comp_score > 21:
            print(f"The computer's hand is {comp_hand}, with a score of {comp_score}. You win!")
          elif comp_score > player_score:
            print(f"The computer's hand is {comp_hand}, with a score of {comp_score}. You lose!")
          elif comp_score < player_score:
            print(f"The computer's hand is {comp_hand}, with a score of {comp_score}. You win!")
          elif comp_score == player_score:
            print(f"The computer's hand is {comp_hand}, with a score of {comp_score}. It's a tie!")
    play_again = input("Would you like to play again? Enter 'yes' or 'no': ").lower()
    if play_again == "yes":
      clear_console()
      blackjack()
    if play_again == "no":
      print("Thanks for playing!")

blackjack()
