import database
import time

database.connect()
user_id = 0
user_balance = 0


def login(username, password):
    global user_id
    global user_balance
    database.cur.execute('SELECT * FROM user WHERE username = ? and password = ?', (username, password))
    user_details = database.cur.fetchone()
    if user_details is not None:
        user_id = user_details[0]
        time.sleep(1)
        print("Login success!")
        user_balance = user_details[3]
    else:
        print("No user found with given details!")
        exit()


def update_balance(updated_balance):
    database.cur.execute("UPDATE user SET balance = ? WHERE id = ?", (updated_balance, user_id))
    database.conn.commit()
