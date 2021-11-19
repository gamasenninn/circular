import requests
import json


print("\n------API Get /r/members ----")

response = requests.get("http://localhost:5010/r/members")
print(response.text)


print("\n------API Get /r/member/{id} ----")

response = requests.get("http://localhost:5010/r/member/1")
print(response.text)


print("\n------API POST /r/member ----")

data = {
    'name': "POST FROM WEB",
    'category': "Web",
    'telNumber': "000-9999-8888",
    'memo': "POST",
    'email': "mail",
}
response = requests.post(
    'http://localhost:5010/r/member',
    json.dumps(data),
    headers={'Content-Type': 'application/json'})

dict_d = json.loads(response.text)
new_id = dict_d['id']
print(new_id, dict_d)

print("\n------API PUT /r/member/{id} ----")

data = {
    'name': "Change POST FROM WEB",
    'category': "Web",
    'telNumber': "000-9999-8888",
    'memo': "PUT",
    'email': "mail",
}
response = requests.put(
    f'http://localhost:5010/r/member/{new_id}',
    json.dumps(data),
    headers={'Content-Type': 'application/json'})

dict_d = json.loads(response.text)
print(dict_d)

response = requests.get(f"http://localhost:5010/r/member/{new_id}")
print(response.text)






'''
print("\n------API Get /api/納品明細 ----")

response = requests.get("http://localhost:5000/api/納品明細")
print(response.text)

print("\n------API Post /api/納品 ----")
data = {'納品日': "2021/01/03",'納品先': "XYZ商店",'担当者': "小野",'摘要': "POST"}
response = requests.post(
    'http://localhost:5000/api/納品',
    json.dumps(data),
    headers={'Content-Type': 'application/json'})
print(response.text)

print("\n------API Put /api/納品 ----")
data = {'ID':1,'納品日': "2021/01/03",'納品先': "PUT商店",'担当者': "小野",'摘要': "PUT"}
response = requests.put(
    'http://localhost:5000/api/納品',
    json.dumps(data),
    headers={'Content-Type': 'application/json'}
    )
print(response.text)

print("\n------API Delete /api/納品 ----")
response = requests.delete(
    'http://localhost:5000/api/納品/6',
    headers={'Content-Type': 'application/json'})
print(response.text)
'''
