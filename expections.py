from typing import Optional


class BadRequestException(Exception):
    def __init__(self, message: str, args=None, code: Optional[int] = None, ):
        self.message = message
        self.code = code or 404

