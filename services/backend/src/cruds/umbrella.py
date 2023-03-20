from abc import ABC
from typing import List

from fastapi import HTTPException
import pymysql
from sqlalchemy.orm import Session

from src.bases.umbrella import UmbrellaBase
from src.models.umbrella import Umbrella
from src.schemas.umbrella import UmbrellaDTO

from src.models.admin import Admin

pymysql.install_as_MySQLdb()


class UmbrellaCrud(UmbrellaBase, ABC):
    def __init__(self, db: Session, token: str):
        self.db: Session = db
        self.admin = self.db.query(Admin).filter(Admin.token == token).first()
        if not self.admin:
            raise HTTPException(status_code=401, detail="Invalid token")

    def add_umbrella(self, request_umbrella: UmbrellaDTO) -> str:
        umbrella = Umbrella(**request_umbrella.dict())
        if umbrella.image_url is not None:
            self.db.add(umbrella)
            self.db.commit()
            message = "SUCCESS: 우산 등록 완료"
        else:
            message = "FAILURE: 우산 등록 실패"
        return message

    def update_umbrella(self, request_umbrella: UmbrellaDTO) -> str:
        update = self.db.query(Umbrella). \
            filter(Umbrella.umb_id == request_umbrella.umb_id). \
            update(request_umbrella.dict(exclude_unset=True),
                   synchronize_session=False)
        if update:
            self.db.commit()
            message = "SUCCESS: 우산 수정 완료"
        else:
            message = "FAILURE: 우산 수정 실패"
        return message

    def delete_umbrella(self, umb_id: int) -> str:
        umbrella_id = self.find_umbrella_by_id(umb_id)
        if umbrella_id:
            self.db.delete(umbrella_id)
            self.db.commit()
            message = "SUCCESS: 우산 삭제 완료"
        else:
            message = "FAILURE: 우산 삭제 실패"
        return message

    def find_all_umbrellas(self) -> List[Umbrella]:
        return self.db.query(Umbrella).all()

    def find_umbrella_by_id(self, umb_id: int) -> UmbrellaDTO:
        return self.db.query(Umbrella).filter(Umbrella.umb_id == umb_id).first()

    def count_all_umbrellas(self) -> int:
        return self.db.query(Umbrella).count()
