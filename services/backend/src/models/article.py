from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey

from src.database import Base
from src.models.mixins import TimestampMixin


class Article(Base, TimestampMixin):

    __tablename__ = "articles"
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    text = Column(String(20), nullable=False)
    reply_id = Column(Integer, nullable=True)
    reference_url = Column(String(256), nullable=True)

    admin_id = Column(String(30), ForeignKey("admins.admin_id"), nullable=True)
    user_id = Column(String(30), ForeignKey("users.user_id"), nullable=True)

    user = relationship('User', back_populates='articles')
    admin = relationship('Admin', back_populates='articles')

    class Config:
        arbitrary_types_allowed = True