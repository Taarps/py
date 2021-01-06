from replit import clear
from art import logo
import operator

#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the blind auction game!")

repeat = True
players = {}

def calculate_highest_price(p):
  winer = max(p.items(), key=operator.itemgetter(1))[0]
  print(f"Congrats the winder of this round {winer} with amount ${bid}!")

while repeat:
  name = input("Please enter your name: ")
  bid = int(input("Please enter your bid amount: $"))
  players[name] = bid
  more_players = input("Are there others who want to bid? ").lower()
  if more_players == "no":
    repeat = False
    calculate_highest_price(p = players)
  else:
    clear()