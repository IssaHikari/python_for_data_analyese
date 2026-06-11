import requests
import os
from PIL import Image
# from IPython.desplay import IFrame

url = 'https://www.ibm.com/'

r=requests.get(url)

print(type(r))

print(r.status_code)

# print(r.headers)

print(r.headers['Content-Type'])

print(r.url)

print(r.encoding)

# print(r.text)

url = "https://www.ibm.com/images/logo.png"

r = requests.get(url)

print(r.content)

with open("image.txt" , "wb") as file:
    file.write(r.content)


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png"


r = requests.get(url)

print(r.headers)

path = os.path.join(os.getcwd() , "image.png")
print(path)

with open(path , "wb") as f:
    f.write(r.content)

Image.open(path)


url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
path = os.path.join(os.getcwd() , "example1.txt")
r=requests.get(url)
with open(path , "wb") as f:
    f.write(r.content)

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

print(r.url)
print("request body:", r.request.body)
print(r.status_code)
print(r.text)
r.headers['Content-Type']
r.json()
print(r.json()['args'])


# Post Requests

url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
# print("GET request body:",r.request.body)
print("POST request URL:", r_post.url)  # Use r_post instead of response

print(r_post.json()['form'])