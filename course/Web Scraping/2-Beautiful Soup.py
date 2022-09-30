import requests
from bs4 import BeautifulSoup
import re

# Example 1
url = "https://en.wikipedia.org/wiki/Mao_Zedong"

response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")

# 1.find method
print(content.find("h1"))
print(content.find("h2").get("id"))
print(content.find("h1").attrs)
print(content.find("h1").text)
print(content.find("h1").name)
print(content.find(attrs={"role": "main"}))
print(content.find(class_="mv_indicator"))

# 2.find_all method
print(content.find_all(["h1", "h2"]))
print(content.find_all("h2", limit=5))

# 3.find with regex
print(content.find(re.compile("^d")))

# 4.elect method
print(content.select("li>a[title=Benjamin Tucker]"))

# Example 2
bs = BeautifulSoup("<h1>Hello World!</h1>")
print(bs.prettify())
print(bs.find(text="Hello World!"))
print(bs.find_all(name="h1"))
