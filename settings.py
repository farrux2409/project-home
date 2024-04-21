from time import time_ns
import bcrypt


def generation_id():
    return str(time_ns())

print(generation_id())
def encoded_password(raw_password: str):
    hash_password = raw_password.encode("utf-8")
    salt = bcrypt.gensalt(6)
    return str(bcrypt.hashpw(hash_password, salt))

# password = 'password123'
# encoded_password = password.encode('utf-8')
# salt = bcrypt.gensalt(4)
#
# hash_password = bcrypt.hashpw(encoded_password, salt)
#
# new_my_password = input('Enter new password: ').encode('utf-8')
#
# result = bcrypt.checkpw(new_my_password, hash_password)
# print(result)
