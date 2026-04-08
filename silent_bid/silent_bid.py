import silent_bid_art
print(silent_bid_art.art)
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("enter your name: ")
    price = int(input("what is your bid? : "))
    bids[name] = price
    should_continue = input("are there any other bidders? type 'yes' or 'no' : ").lower()
    print("\n"*100)
    if should_continue=="no":
        continue_bidding = False
    

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print("winner is:",winner)

find_highest_bidder(bids)
