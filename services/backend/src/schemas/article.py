from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ArticleVO(BaseModel):
    class Config:
        orm_mode = True


class ArticleDTO(ArticleVO):
    article_id: Optional[int]
    title: Optional[str]
    type: Optional[str]
    text: Optional[str]
    reply_id: Optional[int]
    reference_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ArticleCreateDTO(ArticleDTO):
    title: str
    type: str
    text: str
    reference_url: Optional[str]
