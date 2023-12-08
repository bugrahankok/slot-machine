import random
import time
import authentication

payout = {
    "1_bronze": 0.5,
    "2_bronze": 1,
    "3_bronze": 3,
    "3_silver": 10,
    "3_gold": 20,
    "3_diamond": 1000
}

diamond_symbol = "\U0001F48E"
gold_symbol = "\U0001F3C6"
silver_symbol = "\U0001F948"
bronze_symbol = "\U0001F949"

diamond_array = [diamond_symbol, diamond_symbol, diamond_symbol]
gold_array = [gold_symbol, gold_symbol, gold_symbol]
symbols = [diamond_symbol, gold_symbol, silver_symbol, bronze_symbol, gold_array, diamond_array]


def has_nested_list(array, subarray):
    return any(isinstance(item, list) and item == subarray for item in array)


def decide_winner(winner_symbols, bet):

    payout_result = 0

    if has_nested_list(winner_symbols, diamond_array) >= 1:
        payout_result = payout.get("3_diamond")
    elif has_nested_list(winner_symbols, gold_array) >= 1:
        payout_result = payout.get("3_gold")
    elif winner_symbols.count(diamond_symbol) == 3:
        payout_result = payout.get("3_diamond")
    elif winner_symbols.count(gold_symbol) == 3:
        payout_result = payout.get("3_gold")
    elif winner_symbols.count(silver_symbol) == 3:
        payout_result = payout.get("3_silver")
    elif winner_symbols.count(bronze_symbol) == 3:
        payout_result = payout.get("3_bronze")
    elif winner_symbols.count(bronze_symbol) == 2:
        payout_result = payout.get("2_bronze")
    elif winner_symbols.count(bronze_symbol) == 1:
        payout_result = payout.get("1_bronze")

    if payout_result == 0:
        new_balance = authentication.user_balance - bet
        print("No wins for today huh?")
    else:
        winnings = (bet * payout_result)
        new_balance = authentication.user_balance + winnings
        print(winner_symbols)
        print(f"YOU WON {winnings}!")
        print(f"Current balance: {new_balance}!")

    authentication.update_balance(new_balance)


def animation():
    fake_symbols = symbols[:4]
    for i in range(5):
        time.sleep(0.3)
        slot1 = random.choices(fake_symbols, weights=(11, 10, 10, 10))
        slot2 = random.choices(fake_symbols, weights=(11, 10, 10, 10))
        slot3 = random.choices(fake_symbols, weights=(11, 10, 10, 10))
        print("|" + slot1[0] + "|" + slot2[0] + "|" + slot3[0] + "|")


def slot():
    print(f"Balance:{authentication.user_balance}")
    bet = input("Enter your bet:")

    if bet.isdigit():
        bet = int(bet)

        if bet > authentication.user_balance:
            print("Insufficient amount!")

        else:
            print(f"Your bet: {bet}")
            print("Machine started!")
            animation()
            winner_symbols = random.choices(symbols, weights=(5, 20, 30, 100, 5, 1), k=3)
            decide_winner(winner_symbols, bet)

    else:
        print("Invalid bet!")


def add_balance():
    amount = input("How much you want to deposit:")

    if amount.isdigit():
        amount = int(amount)
        balance = authentication.user_balance + amount
        print(f"Balance:{balance}")
    else:
        print("Invalid amount!")


def display_payout_table(payouts):
    for key, value in payouts.items():
        formatted_key = key.replace("_", " ").capitalize()
        print(f"{formatted_key} : {value}")


def start():
    slot_menu_choice = input("1.Play\n2.Add Balance\n3.Exit\n")

    if slot_menu_choice == "1":
        while True:
            slot()
            again = input("Want to play again? (n to quit, any key to continue):")

            if again == "n":
                break
            else:
                pass

    elif slot_menu_choice == "2":
        add_balance()

    elif slot_menu_choice == "3":
        for i in "Good Bye!":
            time.sleep(0.1)
            print(i)
            exit()

    else:
        print("Invalid Option!")
