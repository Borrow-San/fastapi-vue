from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey

from src.database import Base


class Stand(Base):

    __tablename__ = "stands"
    stand_id = Column(Integer, autoincrement=True, primary_key=True)
    district = Column(String(20), nullable=False)
    latitude = Column(Integer, nullable=False)
    longitude = Column(Integer, nullable=False)

    admin_id = Column(String(30), ForeignKey("admins.admin_id"), nullable=True)

    umbrellas = relationship('Umbrella', back_populates='stand')
    admin = relationship('Admin', back_populates='stands')

    class Config:
        arbitrary_types_allowed = True