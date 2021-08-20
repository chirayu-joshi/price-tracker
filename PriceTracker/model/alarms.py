import sqlite3


def check_url(URL):
    conn = sqlite3.connect('PriceTracker.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS alarms (
              product_title text,
              product_url text,
              alarm_price integer,
              current_price integer
            );""")
    conn.commit()

    c.execute("SELECT * FROM alarms WHERE product_url=?", (URL,))
    alarms = c.fetchone()
    conn.close()

    if alarms != None:
        return True
    else:
        return False


def create_alarm(title, url, alarm_price, current_price):
    conn = sqlite3.connect('PriceTracker.db')
    c = conn.cursor()

    c.execute("INSERT INTO alarms VALUES (?, ?, ?, ?)",
              (title, url, alarm_price, current_price))
    conn.commit()

    conn.close()


def read_alarms():
    conn = sqlite3.connect('PriceTracker.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS alarms (
              product_title text,
              product_url text,
              alarm_price integer,
              current_price integer
            );""")
    conn.commit()

    c.execute("SELECT * FROM alarms")
    alarms = c.fetchall()

    conn.close()
    return alarms


def delete_alarm(URL):
    conn = sqlite3.connect('PriceTracker.db')
    c = conn.cursor()

    c.execute("DELETE FROM alarms WHERE product_url=?", (URL,))
    conn.commit()

    conn.close()
