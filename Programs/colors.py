import pyfiglet
from termcolor import colored
import colorama

colorama.init()

text = input("What text do you want to print? ")
color = input("What color? ")

colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

if color not in colors:
    color = 'yellow'

colored_text = colored(pyfiglet.figlet_format(text), color=color)

print(colored_text)
