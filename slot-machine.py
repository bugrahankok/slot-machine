# gecici notlar:
# diamond emoji \U0001F48E
# bronze emoji \U0001F949
# silver emoji \U0001F948
# gold emoji \U0001F3C6
"""
1 bronze : 0.5
2 bronze : 1
3 bronze : 3
3 silver : 10
3 gold : 20
3 diamond: 1000
"""

import random 
import time
import sqlite3

try:
    # SQLite veritabanına bağlan
    conn = sqlite3.connect('slot_machine.sqlite3')

    cur = conn.cursor()

    print("Veritabanına başarıyla bağlandı.")

except sqlite3.Error as e:
    print("SQLite Hatası:", e)

payout = { # payout rates
    "1_bronze" : 0.5,
    "2_bronze" : 1,
    "3_bronze" : 3,
    "3_silver" : 10,
    "3_gold" : 20,
    "3_diamond" : 1000
}

diamond = ["\U0001F48E", "\U0001F48E", "\U0001F48E"]
gold = ["\U0001F3C6", "\U0001F3C6", "\U0001F3C6"]
symbols = ["\U0001F48E", "\U0001F3C6", "\U0001F948", "\U0001F949", gold, diamond]
fake_symbols = ["\U0001F48E", "\U0001F3C6", "\U0001F948", "\U0001F949"]

def has_nested_list(lst, sublist_name):
    return any(isinstance(item, list) and item == sublist_name for item in lst)

def check_winner(winner_symbols, bet):
    global balance
    if has_nested_list(winner_symbols, diamond) >= 1:
        print("\U0001F48E, \U0001F48E, \U0001F48E \n HUGE Jackpot!")
        bet = bet * payout.get("3_diamond")
        print(f"WIN:{bet}")
        balance = balance  + bet 
        return
    
    elif has_nested_list(winner_symbols, gold) >= 1:
        print(winner_symbols)
        print("\U0001F3C6,\U0001F3C6,\U0001F3C6 Jackpot!")
        bet = bet * payout.get("3_gold")
        print(f"WIN: {bet}")
        balance = balance + bet
        return 

    diamond_count = winner_symbols.count("\U0001F48E")
    gold_count = winner_symbols.count("\U0001F3C6")
    silver_count = winner_symbols.count("\U0001F948")
    bronze_count = winner_symbols.count("\U0001F949")

    if winner_symbols == symbols[4]:
        print(winner_symbols)
        print("HUGE JACKPOT!")
        bet = bet * payout.get("3_diamond")
        print(f"WIN:{bet}")
        balance = balance  + bet

    elif gold_count == 3:
        print(winner_symbols)
        print("\U0001F3C6 jackpot")
        bet = bet * payout.get("3_gold")
        print(bet)
        balance = balance + bet

    elif silver_count == 3:
        print(winner_symbols)
        print("\U0001F948 jackpot")
        bet = bet * payout.get("3_silver")
        print(bet)
        balance = balance + bet

    elif bronze_count == 3:
        print(winner_symbols)
        print("\U0001F949 jackpot")
        bet = bet * payout.get("3_bronze")
        print(bet)
        balance = balance + bet

    elif bronze_count == 2:
        print(winner_symbols)
        print("\U0001F949 pair")
        bet = bet * payout.get("2_bronze")
        print(bet)
        balance = balance + bet
        
    elif bronze_count == 1:
        print(winner_symbols)
        print("\U0001F949 win")
        bet = bet * payout.get("1_bronze")
        print(bet)
        balance = balance + bet

    else:
        print(winner_symbols)
        print("No wins for today huh?")
        balance = balance - bet
        

    print(balance)
    return balance


def animation():
    for i in range(5):
        time.sleep(0.3)
        slot1 = random.choices(fake_symbols, weights = (11, 10, 10, 10))
        slot2 = random.choices(fake_symbols, weights = (11, 10, 10, 10))
        slot3 = random.choices(fake_symbols, weights = (11, 10, 10, 10))
        print("|"+ slot1[0] +"|"+ slot2[0] +"|"+ slot3[0] +"|")

def slot():
    print(f"Balance:{balance}")
    bet = input("Enter your bet:")

    if bet.isdigit():
     bet = int(bet)

     if bet > balance:
        print("Insufficient amount!")

     else:
        print(f"Your bet: {bet}")
        print("Machine started!")
        animation()
        winner_symbols = random.choices(symbols, weights = (11, 10, 10, 10, 3, 1), k=3)
        check_winner(winner_symbols, bet)

    else:
        print("Invalid bet!")
        
def add_balance():
    global balance
    amount = input("How much you want to deposit:")

    if amount.isdigit():
        amount = int(amount)
        balance = balance + amount
        print(f"Balance:{balance}")

    else:
        print("Invalid amount!")

def display_payout_table(payout):
    for key, value in payout.items():
        formatted_key = key.replace("_", " ").capitalize()
        print(f"{formatted_key} : {value}")

while True:
    print()
    print("Winning Rates:")
    display_payout_table(payout)  
    print("---------------")
    login_name = str(input("Enter Your Username: "))
    login_password = input("Enter Your Password: ")
    cur.execute('SELECT * FROM user WHERE name = ?', (login_name,))
    name_details = cur.fetchone()
    cur.execute('SELECT * FROM user WHERE password = ?', (login_password,))
    password_details = cur.fetchone()
    if name_details and password_details:
        user_name = name_details[0]
        print(user_name)
        password = password_details[1]
        print(password)
        print("giriş başarıyla tamamlandı")
        cur.execute('SELECT balance FROM user WHERE name = ? and password = ?', (user_name, password))
        balance = cur.fetchone()
        print(balance)
    else:
        print("Geçersiz kullanıcı adı!")
        break 
    menu_choice = input("1.Play\n2.Add Balance\n3.Exit\n")
    
    if menu_choice == "1":
             while True:
                slot()
                again = input("again?(n to quit, anykey to continue):").lower()

                if again == "n":
                   break
             
                else:
                   pass

    elif menu_choice == "2":
        add_balance()

    elif menu_choice =="3":
        for i in "Good Bye!":
            time.sleep(0.13)
            print(i)
        break

    else:
        print("Invalid Option!")

if conn:
        conn.close()
        print("Bağlantı kapatıldı.")

# oyun menusu acildiginda payout tablosu yazdirmamiz lazim!!!!!!  (Eklendi)
# diamond_count degiskeni kullanilmiyor onunla ne yapacagima dair bir fikrim yok  (Düzeltildi)