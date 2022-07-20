import requests
import json
from datetime import datetime
from pprint import pprint
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8000/posts'
HEADERS = {'Content-type': 'application/json'}


class Post():
    id = ''

    @classmethod
    def create(cls):
        title = input('Title: ')
        description = input('Description: ')
        created_at = input('Created at: yy-mm-dd-hh-mm-ss: ')
        updated_at = input('Created at: yy-mm-dd-hh-mm-ss: ')
        post = {
            'title': title,
            'description': description,
            'created_at': created_at,
            'updated_at': updated_at
        }
        print(json.dumps(post))
        try:
            res = requests.post(BASE_URL+'/', auth=BASIC_AUTH,
                                data=json.dumps(post), headers=HEADERS)
            return res.json()
        except Exception as err:
            print(f'Error when create a new post {err}')

    @classmethod
    def get(cls):
        cls.id = input('Id: ')
        query = BASE_URL + '/' + str(cls.id) + '/'
        res = requests.get(query, auth=BASIC_AUTH)
        return res.json()

    @classmethod
    def update(cls):
        old_post = cls.get()
        pprint(old_post)

        title = input('Title: ')
        description = input('Description: ')
        created_at = input('Created at: yy-mm-dd-hh-mm-ss: ')
        updated_at = input('Created at: yy-mm-dd-hh-mm-ss: ')

        title = title if title else old_post['title']
        description = description if description else old_post['description']
        created_at = created_at if created_at else old_post['created_at']
        updated_at = updated_at if updated_at else old_post['updated_at']

        post = {
            'title': title,
            'description': description,
            'created_at': created_at,
            'updated_at': updated_at
        }

        try:
            res = requests.put(BASE_URL+'/' + str(cls.id) + '/', auth=BASIC_AUTH,
                               data=json.dumps(post), headers=HEADERS)
            return res.json()
        except Exception as err:
            print(f'Error when create a new post {err}')

    @classmethod
    def delete(cls):
        cls.id = input('Id: ')
        query = BASE_URL + '/' + str(cls.id) + '/'
        res = requests.delete(query, auth=BASIC_AUTH)
        return 'status code :' + str(res.status_code)


class PostList():
    @classmethod
    def get(cls):
        res = requests.get(BASE_URL, auth=BASIC_AUTH)
        return res.json()


if __name__ == '__main__':
    USERNAME = input('User name: ')
    PASSWORD = input('Password: ')
    BASIC_AUTH = HTTPBasicAuth(USERNAME, PASSWORD)
    while True:
        print("""
                1. Get list of posts
                2. Get a post
                3. Create a new post
                4. Update a post
                5. Delete a post
                0. Exit
                """)
        choose = int(input('Choose: '))
        match choose:
            case 0:
                break
            case 1:
                pprint(PostList.get())
            case 2:
                pprint(Post.get())
            case 3:
                pprint(Post.create())
            case 4:
                pprint(Post.update())
            case 5:
                pprint(Post.delete())
            case default:
                break
