import os
from art import logo
#instructions were to create a dictionary with each bidder as a key and their bid as the value
#i did not follow instructions initially (oops) and built the program a diff way
#i have left that code here
#sorry it looks so clunky, i just want to keep a record of my progress
#but i did redo it the way this lesson was assigned

print(logo)

#list_1 = []
#list_2 = []

#def add_to_list(bid_name, bid_amount):
  #list_1.append(bid_name)
  #list_2.append(bid_amount)

def clear_console():
  return os.system("clear")

dictionary = {}
def add_to_list(bid_name, bid_amount):
  dictionary[bid_name] = bid_amount


stop = False

while stop == False:
  print("Welcome to the silent auction!")
  name = input("What is your name?: ")
  bid = int(input("How much are you bidding?: $"))
  again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  add_to_list(name, bid)
  clear_console()
  if again == "no":
    stop = True

highest = 0
winner = ""

for i in dictionary:
  if dictionary[i] > highest:
    highest = dictionary[i]
    winner = i

    

#dictionary = {"names":list_1}
#dictionary["bids"] = list_2

#max_bid = max(dictionary["bids"])
#max_bid_pos = dictionary["bids"].index(max_bid)
#highest_bidder = dictionary["names"][max_bid_pos]

print(f"Congratulations, {winner}, your bid of ${highest} has won you the auction!")
print('''
                                         .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *
      ''')
