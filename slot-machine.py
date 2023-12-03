import random 
import time

symbols = ["diamond", "gold", "silver"]
balance = 1000

def check_winner (winner_symbol):
    if len(set(winner_symbol)) == 1:
        print("3 Katı")
    elif len(set(winner_symbol)) == 2:
        print("2 katı")
    else: 
        print("zort")
        
def slot ():
    bet = input("Enter your bet: ")
    print("Your bet: " + bet)
    print("Machine started!")
    time.sleep(2)
    winner_symbol = random.choices(symbols, weights = (1, 5, 10), k=3)
    print(winner_symbol)
    
    check_winner(winner_symbol)

slot()