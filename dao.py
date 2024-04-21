import json

from app.model import User
from app.exceptions import BadRequestException


def read_user_all():
    with open('db/users.json', 'r') as f:
        users = json.load(f)

    return users


def read_user_by_user_id(user_id: str):
    users = read_user_all()
    for _id, user in users.items():
        if _id == user_id:
            return user
    raise BadRequestException(f'"{user_id}" not found')


def update_user(user_id: str):
    users = read_user_all()
    for _id, user in users.items():
        if _id == user_id:
            user['full_name'] = input('Enter your full name: ')
            user['password'] = input('Enter your password: ')
            with open('db/users.json', 'w') as f:
                json.dump(users, f, indent=4)
            return True
    return False


def delete_user(user_id: str):
    users = read_user_all()
    if user_id in users.keys():
        users.pop(user_id)
        with open('db/users.json', 'w') as f:
            json.dump(users, f, indent=4)
        return True
    return False





def create_user(user: User):
    users = read_user_all()
    with open('db/users.json', 'w') as f:
        users[user.user_id] = user.__dict__
        json.dump(users, f, indent=4)

