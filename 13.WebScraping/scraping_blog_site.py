import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.rithmschool.com/blog'

response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all('article')
# print(articles)

with open('blog_data.csv', "w") as file:
    csv_writer = writer(file)
    headers = ["title", "link", "date"]
    csv_writer.writerow(headers)

    for article in articles:
        a_tag = article.find('a')
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find('time')["datetime"]
        csv_writer.writerow([title, url, date])
