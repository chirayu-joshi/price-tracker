import sqlite3
from PriceTracker.view import clear, colorText


def change_preferences():
    conn = sqlite3.connect('PriceTracker.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS prefs (
                receiver_email text,
                time_interval_to_check integer
              );""")
    conn.commit()

    c.execute("""SELECT * FROM prefs""")
    prefs = c.fetchone()

    if prefs != None:
        clear()
        print(colorText('[[yellow]]Current settings:[[magenta]]'))
        print('Receiver Email: ' + prefs[0])
        print('Time interval to check updates: ' + str(prefs[1]) + 'seconds')
        user_input = input(
            colorText('[[blue]]Would you like to change preferences? [y/n] [[cyan]]'))
        if user_input == 'y':
            user_email = input(colorText('[[magenta]]Email > [[cyan]]'))
            ttu = int(input(
                colorText('[[magenta]]Time to update (hours) > [[cyan]]')))
            c.execute(
                "UPDATE prefs SET receiver_email=?, time_interval_to_check=?", (user_email, ttu * 60 * 60))
            conn.commit()
    else:
        clear()
        print(colorText('[[yellow]]What are your preferences?[[magenta]]'))
        user_email = input(colorText('[[magenta]]Email > [[cyan]]'))
        ttu = int(
            input(colorText('[[magenta]]Time to update (hours) > [[cyan]]')))
        c.execute("INSERT INTO prefs VALUES (?, ?)",
                  (user_email, ttu * 60 * 60))
        conn.commit()

    conn.close()
