from enum import Enum
from typing import Optional
from enums import Language
from datetime import datetime


class User:
    def __init__(self,
                 full_name: str,
                 password: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 language: Optional[Language] = None,
                 user_id: Optional[str] = None,
                 email: Optional[str] = None,
                 ):
        self.full_name = full_name
        self.password = password
        self.created_at = created_at or str(datetime.now())
        self.language = language or Language.English.value
        self.user_id = user_id
        self.email = email
        print('successfully updated ')


