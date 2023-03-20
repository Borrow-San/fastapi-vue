from abc import ABC
from typing import List

from fastapi import HTTPException
import pymysql
from sqlalchemy.orm import Session

from src.bases.stand import StandBase
from src.models.stand import Stand
from src.schemas.stand import StandDTO

from src.models.admin import Admin

pymysql.install_as_MySQLdb()


class StandCrud(StandBase, ABC):
    def __init__(self, db: Session, token: str):
        self.db: Session = db
        self.admin = self.db.query(Admin).filter(Admin.token == token).one_or_none()
        if self.admin is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    def add_stand(self, request_stand: StandDTO) -> str:
        stand = Stand(**request_stand.dict())
        district = self.db.query(Stand).filter(Stand.district == request_stand.district).one_or_none()
        if district is None:
            self.db.add(stand)
            self.db.commit()
            message = "SUCCESS: 대여소 등록 완료"
        else:
            message = "FAILURE: 대여소 등록 실패"
        return message

    def update_stand(self, request_stand: StandDTO) -> str:
        update = self.db.query(Stand). \
            filter(Stand.stand_id == request_stand.stand_id). \
            update(request_stand.dict(exclude_unset=True),
                     synchronize_session=False)
        if update:
            self.db.commit()
            message = "SUCCESS: 대여소 수정 완료"
        else:
            message = "FAILURE: 대여소 수정 실패"
        return message

    def delete_stand(self, stand_id: int) -> str:
        stand = self.find_stand_by_id(stand_id)
        if stand:
            self.db.delete(stand)
            self.db.commit()
            message = "SUCCESS: 대여소 삭제 완료"
        else:
            message = "FAILURE: 대여소 삭제 실패"
        return message

    def fina_all_stands(self) -> List[Stand]:
        return self.db.query(Stand).all()

    def find_stand_by_id(self, stand_id: int) -> StandDTO:
        return self.db.query(Stand).filter(Stand.stand_id == stand_id).first()
