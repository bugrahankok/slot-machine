import sqlite3

cur: sqlite3.Cursor
conn: sqlite3.Connection


def connect():
    global cur
    global conn
    try:
        conn = sqlite3.connect('slot_machine.sqlite3')
        cur = conn.cursor()

        print("Veritabanına başarıyla bağlandı.")

    except sqlite3.Error as e:
        print("Veritabanına bağlanılamadı!", e)


def kill():
    if conn:
        conn.close()
        print("Bağlantı kapatıldı.")