import sqlite3
from time import sleep
from PriceTracker.controller import check_price, send_mail


def update_alarms():
    conn = sqlite3.connect(
        '/home/wiz/projects/python/PriceTracker/PriceTracker.db')
    c = conn.cursor()

    c.execute("SELECT product_url, current_price FROM alarms")
    old_url_current_prices = c.fetchall()

    url_current_prices = []
    for old_url_current_price in old_url_current_prices:
        curr_price = check_price(old_url_current_price[0])
        if curr_price != old_url_current_price[1]:
            url_current_prices.append(
                (old_url_current_price[0], curr_price))

    for url_current_price in url_current_prices:
        c.execute("UPDATE alarms SET current_price=" +
                  str(url_current_price[1]) + " WHERE product_url=" + url_current_price[0])
        conn.commit()

    conn.close()


def get_eligible_urls():
    conn = sqlite3.connect(
        '/home/wiz/projects/python/PriceTracker/PriceTracker.db')
    c = conn.cursor()

    c.execute("SELECT product_url, alarm_price FROM alarms")
    url_alarm_prices = c.fetchall()

    eligible_urls = []
    for url_alarm_price in url_alarm_prices:
        if check_price(url_alarm_price[0]) <= url_alarm_price[1]:
            eligible_urls.append(url_alarm_price[0])

    conn.close()
    return eligible_urls


def get_user_prefs():
    conn = sqlite3.connect(
        '/home/wiz/projects/python/PriceTracker/PriceTracker.db')
    c = conn.cursor()

    c.execute("SELECT * FROM prefs")
    prefs = c.fetchone()

    conn.close()
    return prefs[0], prefs[1]


while True:
    sleep(60 * 5)  # wait for 5 minutes so that system warms up well

    receiver_email, time_interval = get_user_prefs()

    eligible_urls = get_eligible_urls()
    for eligible_url in eligible_urls:
        send_mail(receiver_email, eligible_url)

    sleep(time_interval)

    update_alarms()
