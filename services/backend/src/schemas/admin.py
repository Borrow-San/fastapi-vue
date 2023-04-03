from pydantic import BaseModel
from typing import List, Optional

from src.schemas.article import ArticleDTO
from src.schemas.rent import RentDTO
from src.schemas.stand import StandDTO
from src.schemas.umbrella import UmbrellaDTO
from src.schemas.user import UserDTO


class AdminVO(BaseModel):
    class Config:
        orm_mode = True


class AdminDTO(AdminVO):
    admin_id: Optional[str]
    name: Optional[str]
    password: Optional[str]
    token: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class AdminLoginDTO(AdminDTO):
    admin_id: str
    password: str
    token: Optional[str]


class AdminCreateDTO(AdminDTO):
    name: str
    password: str


class AdminDeleteDTO(AdminDTO):
    admin_id: str
    token: Optional[str]


class AdminDetail(AdminDTO):
    stands: List[StandDTO] = []
    articles: List[ArticleDTO] = []
    umbrellas: List[UmbrellaDTO] = []
    users: List[UserDTO] = []
    rents: List[RentDTO] = []
