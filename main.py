import time
import authentication
import database
import slot_machine

print("Winning Rates:")
slot_machine.display_payout_table(slot_machine.payout)
print("---------------")
login_name = str(input("Enter Your Username: "))
login_password = str(input("Enter Your Password: "))

authentication.login(login_name, login_password)

menu_choice = input("1. Slot Machine\n2. Roulette\n3. Blackjack 21\n4. Exit\n")

if menu_choice == "1":
    slot_machine.start()
elif menu_choice == "2":
    print("rulet")
elif menu_choice == "3":
    print("blackjack")
elif menu_choice == "4":
    for i in "Good Bye!":
        time.sleep(0.13)
        print(i)

input()
database.kill()