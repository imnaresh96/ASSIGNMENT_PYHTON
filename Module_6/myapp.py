import json
import requests

URL = "http://127.0.0.1:8000/bookinfo/1"

r= requests.get(url=URL)

data=r.json()

print(data)

URL="http://127.0.0.1:8000/bookcreate/"

data={
    'Title':'Karishma',
    'Author':'Rawal',
    'Isbn':'458515',
    'Publisher':'Sharma Education',
}
 
json_data=json.dumps(data)

r=requests.post(url=URL, data=json_data)

data = r.json()

print(data)

#update data
URL="http://127.0.0.1:8000/book_update/"

def get_data(id = None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data=json.dumps(data)
    r= requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)
get_data(2)
