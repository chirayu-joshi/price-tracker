import time
from PriceTracker.model import change_preferences
from PriceTracker.view import display_dashboard, colorText
from PriceTracker.controller import add_alarms, remove_alarms, show_alarms


def main():
    user_input = display_dashboard()

    if user_input == '1':
        add_alarms()
    elif user_input == '2':
        remove_alarms()
    elif user_input == '3':
        show_alarms()
    elif user_input == '4':
        change_preferences()
    elif user_input == '5':
        quit()
    else:
        print(colorText('[[red]]Wrong input. Please try again.'))
    main()


if __name__ == "__main__":
    main()
