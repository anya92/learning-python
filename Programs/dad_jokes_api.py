import requests
import colorama
from termcolor import colored
from pyfiglet import figlet_format as formated
from random import choice

colorama.init()

print(colored(formated("Dad Jokes"), color="magenta"))

term = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={'Accept': "application/json"},
    params={'term': term}
)

data = response.json()

total_jokes = data["total_jokes"]
jokes = data["results"]

if total_jokes == 0:
    print(f"Sorry, I don't have any jokes about {term}. Please try again.")
elif total_jokes == 1:
    print(f"I've found one joke about {term}.")
    print(jokes[0]["joke"])
else:
    print(f"I've got {total_jokes} about {term}. Here is one:")
    print(choice(jokes)["joke"])
