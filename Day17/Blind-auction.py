from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}

biding_finished = False

def find_highest_bidder(biding_record):
  highest_bid = 0
  winner = ""

  for bidder in biding_record:
    bid_amount = biding_record[bidder]
    if highest_bid > bid_amount :
      bid_amount = highest_bid
      winner = bidder
  print(f"the winner is {winner} with the bid amount {bid_amount}")

while not biding_finished :
  name = input("Enter your name? ")
  price = int(input (" How much money to want to bid? $ "))
  bids[name] = price
  should_continue = input("Are there any others bidders? Type yes or no ? ")
  if should_continue == "no":
    biding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

