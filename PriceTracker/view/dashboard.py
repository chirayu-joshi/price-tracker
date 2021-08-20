from PriceTracker.view import clear, colorText


def display_dashboard():
    clear()

    print(colorText('[[yellow]]Welcome to [[green]]PriceTracker![[magenta]]'))
    print('1. Add Alarms')
    print('2. Remove Alarms')
    print('3. Show Alarms')
    print('4. My Settings')
    print('5. Exit')

    user_input = input(colorText('> [[cyan]]'))

    return user_input
