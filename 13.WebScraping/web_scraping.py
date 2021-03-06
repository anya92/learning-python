from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>My page</title>
  </head>
  <body>
    <div id="first">
      <h3 data-example="yes">Site title</h3>
      <p>Some text</p>
    </div>
    <ol>
      <li class="special extra-special">Special item 1</li>
      <li class="special">Special item 2</li>
    </ol>
    <div data-example="yes">End</div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(type(soup))  # <class 'bs4.BeautifulSoup'>

print(soup.body)  # <body> <div id = "first" > (...)

print(soup.find('li'))
# <li class="special">Special item 1</li> (only first)

print(soup.find_all('li'))
# [<li class="special">Special item 1</li>,
#  <li class="special">Special item 2</li>]

print(soup.find(id="first"))
# <div id="first">
# <h3 data-example="yes">Site title </h3>
# <p>Some text</p >
# </div>

print(soup.find_all(class_="special"))
# [<li class="special">Special item 1</li>,
#  <li class="special">Special item 2</li>]

print(soup.find_all(attrs={"data-example": "yes"}))
# [<h3 data-example="yes">Site title</h3>,
#  <div data-example="yes">End</div>]

# CSS selectors

# id
print(soup.select('#first'))  # returns a list
print(soup.select('#first')[0])
# class
print(soup.select('.special'))
# tag name
print(soup.select('div'))
# attribute
print(soup.select('[data-example]'))

# accessing data

el = soup.select('.special')[0]
print(el)  # <li class="special">Special item 1</li>
print(el.get_text())  # 'Special item 1'

print(el.name)  # li
print(el.attrs)  # {'class': ['special', 'extra-special']}

for element in soup.select('.special'):
    print(element.get_text())

    # Special item 1
    # Special item 2


# navigating

print(soup.body.contents)
# ['\n', <div id="first">
#  <h3 data-example = "yes" > Site title < /h3 >, ... ]

print(soup.body.contents[1].next_sibling)  # '\n'
print(soup.body.contents[1].next_sibling.next_sibling)
# <ol>
#   <li class="special extra-special">Special item 1</li>
#   <li class="special">Special item 2</li>
# </ol>

print(soup.find(class_='extra-special').parent)  # <ol>...

print(soup.find(class_='extra-special').parent.parent)  # <body> ...

print(soup.find("h3").find_parent())  # <div id="first"> ...

print(soup.find("h3").find_parent("html"))  # <html> ...

print(soup.find(id="first").find_next_sibling())  # <ol> ...

print(soup.find(id="first").find_next_sibling().find_next_sibling())
# <div data-example="yes">End</div>
