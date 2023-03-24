from typing import List, Optional
from pydantic import BaseModel

from src.schemas.article import ArticleDTO
from src.schemas.rent import RentDTO


class UserVO(BaseModel):
    class Config:
        orm_mode = True


class UserDTO(UserVO):
    user_id: Optional[str]
    name: Optional[str]
    cur_lat: Optional[str]
    cur_lng: Optional[str]
    point: Optional[int]
    password: Optional[str]
    token: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class UserDetail(UserDTO):
    articles: List[ArticleDTO] = []
    rents: List[RentDTO] = []


class UserUpdate(BaseModel):
    user_id: Optional[str]
    name: Optional[str]
    cur_lat: Optional[str]
    cur_lng: Optional[str]
    password: Optional[str]
    token: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True