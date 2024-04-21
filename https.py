from typing import Optional




class Response:
    def __init__(self, data:str, status_code: Optional[int] = None) -> None:
        self.data = data
        self.status_code = status_code or 202
