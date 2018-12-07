import requests
from bs4 import BeautifulSoup
from csv import reader, writer
from random import choice
from termcolor import colored
import colorama  # windows

# scraping quotes

BASE_URL = 'http://quotes.toscrape.com/'


def scrap_quotes():
    quotes = []
    next_url = '/page/1'

    while next_url:
        response = requests.get(BASE_URL + next_url)
        soup = BeautifulSoup(response.text, "html.parser")

        quote_divs = soup.find_all(class_="quote")

        for quote_div in quote_divs:
            quotes.append({
                'text': quote_div.find(class_="text").get_text(),
                'author': quote_div.find(class_="author").get_text(),
                'author_url': quote_div.find("a")["href"]
            })

        next_li = soup.find(class_="next")
        next_url = next_li.find("a")["href"] if next_li else None

    return quotes


quotes = []

try:
    with open('quotes.csv', "r", encoding='utf-8') as file:
        # quotes file already exists
        csv_reader = reader(file)
        for quote in csv_reader:
            quotes.append({
                'text': quote[0],
                'author': quote[1],
                'author_url': quote[2]
            })
except FileNotFoundError as error:
    # there is no quotes file
    with open("quotes.csv", "w", encoding='utf-8', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow(["text", "author", "author_url"])
        quotes = scrap_quotes()
        for quote in quotes:
            csv_writer.writerow(
                [quote["text"], quote["author"], quote["author_url"]])


# print(quotes)

# starting a game

def print_hint(remaining_guesses, quote):
    if remaining_guesses == 3:
        response = requests.get(BASE_URL + quote["author_url"])
        soup = BeautifulSoup(response.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_location = soup.find(
            class_="author-born-location").get_text()
        print(
            f"The author was born in {birth_date} in {birth_location}.")
    elif remaining_guesses == 2:
        print(
            f"The author's first name starts with {quote['author'].split()[0][0]}.")
    elif remaining_guesses == 1:
        print(
            f"The author's last name starts with {quote['author'].split()[-1][0]}.")


def start_game():
    random_quote = choice(quotes)
    correct_answer = random_quote["author"]
    remaining_guesses = 4

    print("Here is a quote:\n")
    colorama.init()  # windows
    colored_quote = colored(
        random_quote["text"], on_color="on_cyan")
    print(colored_quote + '\n')

    user_response = ''

    while user_response.lower() != correct_answer.lower() and remaining_guesses > 0:
        user_response = input(
            f"Who said this? Guesses remaining: {remaining_guesses}. ")

        if user_response == 'quit' or user_response == 'q':
            break

        if user_response.lower() == correct_answer.lower():
            print("You guessed correctly! Congratulations!\n")
            break

        remaining_guesses -= 1
        if remaining_guesses == 3:
            print_hint(remaining_guesses=3, quote=random_quote)
        elif remaining_guesses == 2:
            print_hint(remaining_guesses=2, quote=random_quote)
        elif remaining_guesses == 1:
            print_hint(remaining_guesses=1, quote=random_quote)
        else:
            print(
                f"Sorry, you ran out of guesses. The correct answer was: {correct_answer}.\n")

    play_again = ''
    while play_again not in ('y', 'yes', 'n', 'no'):
        play_again = input("Do you want to keep playing? (y/n) ")
        if play_again in ('y', 'yes'):
            return start_game()
        else:
            print("OK. See you next time!")
            break


start_game()
