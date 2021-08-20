from PriceTracker.view import clear, colorText


def display_alarms(alarms):
    clear()
    if alarms != []:
        print(colorText('[[yellow]]All active alarms:'))

        for alarm in alarms:
            print(colorText(
                '[[blue]]------------------------------------------------[[magenta]]'))
            print('Title: ' + alarm[0])
            print('URL: ' + alarm[1])
            print('Current price: ' + str(alarm[3]))
            print('Your price: ' + str(alarm[2]))

        print(colorText(
            '[[blue]]------------------------------------------------[[magenta]]'))
        print(colorText(
            '[[green-bg]][[white]]================================================[[reset]]'))
        return True
    else:
        print(colorText('[[red]]No active alarm.[[blue]]'))
        return False
