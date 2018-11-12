import requests

url = "https://google.com"
res = requests.get(url)

print(
    f"Your request to {url} came back with status code: {res.status_code}")

# print(response.headers)
# print(response.text)

url_2 = "https://api.github.com/events"

response = requests.get(url_2, headers={
    'Accept': "application/json"
})

data = response.json()

print(type(data))  # <class 'list'>
