# json method ==> dump, dumps, load, loads
import json
from urllib.request import urlopen

# example 1:

with open("38-my.json") as file:
    data = json.load(file)  # convert json to python

for i in data:  # change and manipulate ==> delete age
    del i["age"]
print(data)

with open("newfile.json", "w") as file:
    json.dump(data, file, indent=2)

# example 2:
# work with api:
url = "https://api.exchangeratesapi.io/latest?base=USD"

with urlopen(url) as file:
    data = file.read()
file_data = json.loads(data)

with open("currency.json", "w") as file:
    json.dump(file_data, file, indent=2)
