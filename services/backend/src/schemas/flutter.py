from typing import Optional

from pydantic import BaseModel
from typing import List


class rentDTO(BaseModel):
    token: Optional[str]
    qr_code: Optional[str]

class returnDTO(BaseModel):
    token: Optional[str]
    qr_code: Optional[str]
    image: Optional[List]

class TestDTO(BaseModel):
    image: Optional[List]
