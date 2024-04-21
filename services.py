from app.exceptions import BadRequestException
from app.http import Response
from app.model import User
from app.validators import check_validators
from app.settings import encoded_password, generation_id
import dao


def user_create_service(user: User):
    check_validators(user)
    user.password = encoded_password(user.password)
    user.user_id = generation_id()
    dao.create_user(user)
    response = Response('User created Successfully!', 201)
    if response.data:
        print('User created Successfully!')
    else:
        raise BadRequestException('Bad request', code=404)


# 1.40

def user_update_service():
    user_id = input('Enter user id : ')
    # user_id = str(generation_id())
    result = dao.update_user(user_id)
    # result = str(generation_id())
    if result:
        print('Successfully updated')
    else:
        raise BadRequestException('Bad request', code=404)


# user_update_service()

def user_delete_service():
    user_id = str(input('Enter id: '))
    # user_id = str(generation_id())
    result = dao.delete_user(user_id)
    if result:
        print('Successfully deleted')
    else:
        raise BadRequestException('Bad request', code=404)


def user_read_service():
    user_id = str(input('Enter id:'))
    user = dao.read_user_by_user_id(user_id)
    if user:
        print(user)

user_read_service()