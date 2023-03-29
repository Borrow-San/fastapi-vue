from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi import UploadFile


class RentVO(BaseModel):
    class Config:
        orm_mode = True


class RentDTO(RentVO):
    rent_id: Optional[int]
    disrepair: Optional[int]
    rent_time: Optional[datetime]
    return_time: Optional[datetime]
    admin_id: Optional[str]
    user_id: Optional[str]
    umb_id: Optional[int]

class RentDTOdata(BaseModel):
    token: Optional[str]
    qr_code: Optional[str]

class RentDTOfile(BaseModel):
    image: Optional[UploadFile]