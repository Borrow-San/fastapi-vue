from typing import Optional
from pydantic import BaseModel


class UmbrellaVO(BaseModel):
    class Config:
        orm_mode = True


class UmbrellaDTO(UmbrellaVO):
    umb_id: Optional[int]
    disrepair_bool: Optional[int]
    image_url: Optional[str]
    status: Optional[str]
    qr_code: Optional[str]
    admin_id: Optional[str]
    stand_id: Optional[int]