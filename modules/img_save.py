import requests
from io import BytesIO
from PIL import Image


r = requests.get("https://tse2.mm.bing.net/th?q=Cheesy+Pizza&amp;w=42&amp;h=42&amp;c=1&amp;p=0&amp;pid=InlineBlock&amp;mkt=en-IN&amp;cc=IN&amp;setlang=en&amp;adlt=moderate&amp;t=1")
print("Status :", r.status_code)
img = Image.open(BytesIO(r.content))
print(img.size, img.format, img.mode)
path = "temp 1." + img.format
try:
	img.save(path, img.format)
except IOError:
	print("Cannot save Image")
