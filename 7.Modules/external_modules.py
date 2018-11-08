# https://pypi.org/

# pip install termcolor

# import termcolor

from termcolor import colored
import colorama  # windows

# print(dir(termcolor))

# help(termcolor)

colorama.init()

text = colored("Hello, world", color="cyan", on_color="on_red")

print(text)
