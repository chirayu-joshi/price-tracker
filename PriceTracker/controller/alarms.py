import requests
from PriceTracker.model import check_url, create_alarm, read_alarms, delete_alarm
from PriceTracker.view import clear, colorText, display_alarms
from PriceTracker.controller import get_price_title


def add_alarms():
    #URL = 'https://www.amazon.in/Logitech-Backlit-Mechanical-Keyboard-Pass-Through/dp/B06XR5MWGM/ref=sr_1_3?dchild=1&keywords=mechanical+keyboard+logitech&qid=1607162718&sr=8-3'

    # URL = 'https://www.amazon.in/Logitech-Mechanical-Keyboard-Lightsync-Customizable/dp/B084YX4XJP/ref=sr_1_2?dchild=1&keywords=mechanical+keyboard+logitech&qid=1607162718&sr=8-2'
    clear()
    URL = input(colorText('[[magenta]]URL > [[cyan]]'))
    if check_url(URL) == False:
        print(colorText('[[green]]Fetching Product details...[[magenta]]'))
        try:
            price, title = get_price_title(URL)
        except:
            user_input = input(colorText(
                '[[red]]There was a problem fetching details. Do you wish to retry? [y/n]: [[cyan]]'))
            if user_input == 'y':
                add_alarms()
            return True
        print('Product Title: ' + title)
        print('Product Price: ' + str(price))
        alarm_price = input(colorText('Alarm Price > [[cyan]]'))

        create_alarm(title, URL, alarm_price, price)
        input(
            colorText('[[green]]Alarm successfully set. Press ENTER key to continue: '))
    else:
        print(colorText('[[red]]Alarm with given URL already exist.[[blue]]'))
        input('Press ENTER key to continue: ')


def remove_alarms():
    alarms = read_alarms()
    if display_alarms(alarms) == True:
        URL = input(
            colorText('[[magenta]]Enter URL from above to remove alarm > [[cyan]]'))
        if check_url(URL) == True:
            delete_alarm(URL)
            print(colorText('[[green]]Alarm deleted successfully.'))
        else:
            user_input = input(colorText(
                '[[red]]Entered URL is incorrect. Do you wish to retry? [y/n]: [[cyan]]'))
            if user_input == 'y':
                remove_alarms()
            return True

    input(colorText('[[blue]]Press ENTER key to continue: '))


def show_alarms():
    alarms = read_alarms()
    display_alarms(alarms)
    input(colorText('[[blue]]Press ENTER key to continue: '))
