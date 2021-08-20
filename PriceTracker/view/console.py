from os import system, name

'''
  Refer: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
  for more info about color text formats
'''


COLORS = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m",
    "black-bg": "\u001b[40m",
    "red-bg": "\u001b[41m",
    "green-bg": "\u001b[42m",
    "yellow-bg": "\u001b[43m",
    "blue-bg": "\u001b[44m",
    "magenta-bg": "\u001b[45m",
    "cyan-bg": "\u001b[46m",
    "white-bg": "\u001b[47m",
    "reset-bg": "\u001b[0m"
}


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
