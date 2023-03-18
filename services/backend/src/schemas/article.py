from datetime import datetime
from typing import Optional
import pydantic


class ArticleDTO(pydantic.BaseModel):
    article_id: Optional[int]
    title: Optional[str]
    type: Optional[str]
    text: Optional[str]
    reply_id : Optional[int]
    reference_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True