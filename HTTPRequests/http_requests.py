import requests

url = "https://google.com"
response = requests.get(url)

print(
    f"Your request to {url} came back with status code: {response.status_code}")

# print(response.headers)
# print(response.text)

# requesting JSON

url_2 = "https://icanhazdadjoke.com/"

response_2 = requests.get(url_2, headers={
    # 'Accept': "text/plain"
    'Accept': "application/json"
})

print(response_2.text)

data = response_2.json()

print(type(data))  # <class 'dict'>

print(data["joke"])

# requests with params

url_3 = "https://icanhazdadjoke.com/search"

response_3 = requests.get(
    url_3,
    headers={'Accept': "application/json"},
    params={'term': 'school', 'limit': 1}
)

print(response_3.json()["results"])
