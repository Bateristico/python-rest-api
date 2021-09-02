import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":80, "name": "Camilo", "views": 10000},
{"likes":12, "name": "How to make videos", "views": 123123},
{"likes":100, "name": "How to make a rest api in python", "views": 22}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),  data[i])
    print(response.json())    

# response = requests.put(BASE + "video/1", {"likes":10, "name": "Camilo", "views": 10000})
# print(response.json())
# input()


input()
response - requests.delete(BASE + "video/0")
print(response.json())

input()

response = requests.get(BASE + "video/1")
print(response.json())

