"""
Name: Blind Auction
Version: 1.0
Author: @aemetarom
Purpose: Simulates a blind auction accomodating multiple bidders.
Variables:
dict auction_bids - dictionary of given bidders and bids
str other_bidders - check for continuing to ask for bidder information
bool bidding_finished - flag for disabling the bidder information request loop
str bidder_name - Name of the bidder placing a bid
int bid - the amount to be bid
Functions:
find_highest_bidder(bidding_record): Loops through auction_bids to find the highest bid and the owner of that bid, then
outputs the winner's information.
"""

# Modules
from os import system
from art import logo

# Functions
def find_highest_bidder(bidding_record):
    highest_bidder = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder
    system("cls")
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# Variables
auction_bids = {}
other_bidders = "yes"
bidding_finished = False

# Output
print(logo)
print("Welcome tot he secret auction program.")

while not bidding_finished:
    bidder_name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_bids[bidder_name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == "no":
        bidding_finished = True
        find_highest_bidder(auction_bids)
    elif other_bidders == "yes":
        system("cls")