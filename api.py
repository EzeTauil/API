import requests
res = requests.get("https://randomfox.ca/floof")
print(res.status_code)
fox_img = res.json()
print(fox_img["image"])
url = fox_img["image"]
r = requests.get(url)
file = open("image.png","wb")
file.write(r.content)
