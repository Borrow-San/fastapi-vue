from typing import List

import pymysql
from sqlalchemy.orm import Session
from abc import ABC
from fastapi import HTTPException

from src.bases.rent import RentBase
from src.models.rent import Rent
from src.schemas.rent import RentDTO

from src.models.admin import Admin

pymysql.install_as_MySQLdb()


class RentCrud(RentBase, ABC):
    def __init__(self, db: Session, token: str):
        self.db: Session = db
        self.admin = self.db.query(Admin).filter(Admin.token == token).first()
        if self.admin is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    def add_rent(self, request_rent: RentDTO) -> str:
        rent = Rent(**request_rent.dict())
        if rent.user_id:
            rent.admin_id = self.admin.admin_id
            self.db.add(rent)
            self.db.commit()
            message = "SUCCESS: 대여 기록 추가 완료"
        else:
            message = "FAILURE: 대여 기록 추가 실패"
        return message

    def update_rent(self, request_rent: RentDTO) -> str:
        update = self.db.query(Rent). \
            filter(Rent.rent_id == request_rent.rent_id). \
            update(request_rent.dict(exclude_unset=True),
                   synchronize_session=False)
        if update:
            self.db.commit()
            message = "SUCCESS: 대여 기록 수정 완료"
        else:
            message = "FAILURE: 대여 기록 수정 실패"
        return message

    def delete_rent(self, rent_id: int) -> str:
        rent_id = self.find_rent_by_id(rent_id)
        print("delete_rent 진입")
        if rent_id:
            self.db.delete(rent_id)
            self.db.commit()
            message = "SUCCESS: 대여 기록 삭제 완료"
        else:
            message = "FAILURE: 대여 기록 삭제 실패"
        return message

    def fina_all_rents(self) -> List[Rent]:
        return self.db.query(Rent).all()

    def find_rent_by_id(self, rent_id: int) -> RentDTO:
        return self.db.query(Rent).filter(Rent.rent_id == rent_id).first()

    def count_all_rents(self) -> int:
        return self.db.query(Rent).count()
