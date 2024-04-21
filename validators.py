from app.model import User
from app.exceptions import BadRequestException


def check_validators(user: User):
    if not user.password:
        raise BadRequestException('Password is required')
    if not user.email:
        raise BadRequestException('Email is required')
