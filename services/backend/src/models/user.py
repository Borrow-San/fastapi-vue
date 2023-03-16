from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base
from src.models.mixins import TimestampMixin


class User(Base, TimestampMixin):

    __tablename__ = "users"

    user_id = Column(String(30), primary_key=True)
    age = Column(Integer)
    address = Column(String(20))
    most_use_loc = Column(String(20))
    cur_lat = Column(String(20))
    cur_lng = Column(String(20))
    birth = Column(String(20))
    grade = Column(String(20))
    pay_info = Column(String(20))
    password = Column(String(100), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    gender = Column(String(20), nullable=True)
    token = Column(String(256))

    admin_id = Column(String(30), ForeignKey("admins.admin_id"), nullable=True)

    admin = relationship('Admin', back_populates='users')
    articles = relationship('Article', back_populates='user')
    rents = relationship('Rent', back_populates='user')

    class Config:
        arbitrary_types_allowed = True
