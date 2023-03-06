from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin
from ..database import Base


class Admin(Base, TimestampMixin):
    __tablename__ = "admins"

    admin_id = Column(String(30), primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    token = Column(String(256))

    stands = relationship('Stand', back_populates='admins')
    umbrellas = relationship('Umbrella', back_populates='admins')
    articles = relationship('Article', back_populates='admins')
    users = relationship('User', back_populates='admins')
    rents = relationship('Rent', back_populates='admins')

    class Config:
        arbitrary_types_allowed = True
