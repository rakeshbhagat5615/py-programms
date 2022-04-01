import requests
from bs4 import BeautifulSoup


url = input("Enter URL : ")
name = input("Filename : ")

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

file = open(name + ".html", "w+")
file.write(soup.prettify())