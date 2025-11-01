# Dictionary is combination of key-value pair. We can access value with the help of key
dic = {
    "Anurag":"Human Being",
    "car": "object"
}
print(dic["Anurag"])
print(dic["car"])

info ={'name':'Anurag','age':22,'eligible':True}
# print(info)
# print(info.keys)
# print(info.values())

for key in info.keys():
    print(f"The value crossponding to the key {key} is {info[key]}")



