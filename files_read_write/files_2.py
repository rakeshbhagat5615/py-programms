import os
import simplejson as json


if os.path.isfile("age.json") and os.stat("age.json").st_size != 0:
	old_file = open("age.json", "r+")
	data = json.loads(old_file.read())
	print("current age is", data["age"], "--adding one year")
	data["age"] = data["age"] + 1
	print("new age is", data["age"])
else:
	old_file = open("age.json", "w+")
	data = {"name": "RB", "age": 22}
	print("no file found", "setting defualt age to", data["age"])
	
old_file.seek(0)
old_file.write(json.dumps(data))