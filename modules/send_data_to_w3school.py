import requests


my_data = {"name": "RB", "email": "rakeshbhagat.rb5615@gmail.com"}
r = requests.post("https://tryphp.w3schools.com/showphp.php?filename=demo_form_post", data=my_data)
file = open("w3school.html", "w+")
file.write(r.text)