import requests
from datetime import datetime

TOKEN = "ughgsnhingkgr"
USERNAME = "rakhi123"
pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config ={
    "id" : "graph12",
    "name":"Coding graph",
    "unit": "Hr",
    "type": "float",
    "color":"ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creatin_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph12"
today = datetime.now()
pixels_prams ={
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

response = requests.post(url=pixel_creatin_endpoint,json=pixels_prams,headers=headers)
print(response.text)


update_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/graph12/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity":"4.00"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/graph12/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)