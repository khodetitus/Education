import requests

# request by choose methods
request1 = requests.get("https://httpbin.org/get/", proxies={"https": ""})  # send choose url
request2 = requests.post("https://httpbin.org/post/", data={"key": "value"})
request3 = requests.put("https://httpbin.org/put/", data={"key": "value"})
request4 = requests.delete("https://httpbin.org/delete/")
request5 = requests.head("https://httpbin.org/get/")
request6 = requests.options("https://httpbin.org/get/")

# example 1
url = "https://www.wikipedia.org/"
response = requests.get(url)
print(response.url)  # output -->url = "https://www.wikipedia.org/"
print(response.status_code)  # output --> 200
print(response.request.headers)  # output --> show the url headers
print(response.reason)  # output --> OK
print(response.headers)  # output --> show the response headers
print(response.text)  # output --> show the source code url
