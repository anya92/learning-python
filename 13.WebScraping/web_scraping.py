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
      <li class="special">Special item 1</li>
      <li class="special">Special item 2</li>
    </ol>
    <div data-example="yes">End</div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(type(soup))  # <class 'bs4.BeautifulSoup'>

print(soup.body)  # <body> <div id = "first" > (...)

print(soup.find('li'))  # <li class="special">Special item 1</li> (only first)

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
