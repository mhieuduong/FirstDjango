import requests
from datetime import datetime
from pprint import pprint
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8000/posts'

# login: enter username, password


def create_auth():
    # user = input('Nhap user: ')
    # password = input('Nhap password: ')
    user = 'admin'
    password = 'admin'
    return HTTPBasicAuth(user, password)


# get_list of posts
def get_list_posts(basic_auth):
    res = requests.get(BASE_URL, auth=basic_auth)
    pprint(res.json())


# get_specifc post
def get_a_post(id, basic_auth):
    query = BASE_URL + '/' + str(id) + '/'
    res = requests.get(query, auth=basic_auth)
    print(res)
    pprint(res.json())


# create new post
def create_a_post(basic_auth):
    title = input('Title: ')
    description = input('Description: ')
    created_at = map(input, input().split()) if created_at else datetime.now()
    uploaded_at = map(input, input().split()) if uploaded_at else datetime.now()
    


# update post
# delete post
def delete_a_post(id, basic_auth):
    query = BASE_URL + '/' + str(id) + '/'
    res = requests.delete(query, auth=basic_auth)
    print(res)
    pprint(res.status_code)

if __name__ == '__main__':
    basic_auth = create_auth()
    get_a_post(3, basic_auth)
    delete_a_post(3, basic_auth)
    get_a_post(3, basic_auth)
