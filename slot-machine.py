import random 
import time

diamond = ["diamond", "diamond", "diamond"]
gold = ["gold", "gold", "gold"]
symbols = ["diamond", "gold", "silver", "bronze", gold, diamond]
balance = 1000

def has_nested_list(lst, sublist_name):
    return any(isinstance(item, list) and item == sublist_name for item in lst)

def check_winner(winner_symbols, bet):
    if has_nested_list(winner_symbols, diamond) >= 1:
        print("Diamond, Diamond, Diamond \n Buğra Jackpot")
        return
    elif has_nested_list(winner_symbols, gold) >= 1:
        print("Gold, Gold, Gold \nGold Jackpot")
        return 
    
    diamond_count = winner_symbols.count("diamond")
    gold_count = winner_symbols.count("gold")
    silver_count = winner_symbols.count("silver")
    bronze_count = winner_symbols.count("bronze")

    if winner_symbols == symbols[4]:
        print(winner_symbols)
        print("Buğra jackpot")
    elif gold_count == 3:
        print(winner_symbols)
        print("gold jackpot")
        bet = bet * 1000
        print(bet)
    elif silver_count == 3:
        print(winner_symbols)
        print("silver jackpot")
        bet = bet * 500
        print(bet)
    elif bronze_count == 3:
        print(winner_symbols)
        print("bronze jackpot")
        bet = bet * 200
        print(bet)
    elif bronze_count == 2:
        print(winner_symbols)
        print("bronze pair")
        bet = bet * 50
        print(bet)
    elif bronze_count == 1:
        print(winner_symbols)
        print("bronze win")
        bet = bet * 30
        print(bet)


def slot ():
    bet = int(input("Enter your bet: "))
    print(f"Your bet: {bet}")
    print("Machine started!")
    time.sleep(2)
    winner_symbols = random.choices(symbols, weights = (11, 10, 10, 10, 3, 1), k=3)
    
    check_winner(winner_symbols, bet)

slot()