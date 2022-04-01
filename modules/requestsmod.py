import requests

param = {"q": "facebook"}
r = requests.get("https://www.bing.com/search", params=param)
print("Status :", r.status_code)
print(r.text)
f = open("google.html", "w+")
f.write(r.text)