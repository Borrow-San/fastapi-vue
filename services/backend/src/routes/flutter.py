import os.path
import numpy as np
from PIL import Image
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from src.contents.yolo.detect_fine_umb import detect_fine_umb
from src.database import get_db
from src.env import ROOT_CTX
from src.models.rent import Rent
from src.models.umbrella import Umbrella
from src.models.user import User
from src.schemas.flutter import rentDTO, returnDTO
from src.utils.tools import utc_seoul
from starlette.responses import JSONResponse

router = APIRouter()


@router.post("/rent")
async def rent_umb(dto: rentDTO, db: Session = Depends(get_db)):
    token = dto.dict()["token"]
    qr_code = dto.dict()["qr_code"]
    db_user = db.query(User).filter(User.token == token).one_or_none()
    db_umb = db.query(Umbrella).filter(Umbrella.qr_code == qr_code).one_or_none()
    if db_user is not None and db_umb is not None:
        db_rent = Rent(user_id=db_user.user_id, umb_id=db_umb.umb_id, disrepair=1,
                       rent_time=utc_seoul())
        db.add(db_rent)
        db_umb.status = "대여중"
        db_user.point -= 11000
        db.commit()
        return JSONResponse(status_code=200, content=dict(msg="대여 성공"))
    else:
        return JSONResponse(status_code=200, content=dict(msg="대여 실패"))


@router.post("/return")
async def return_umb(dto: returnDTO, db: Session = Depends(get_db)):
    token = dto.dict()["token"]
    qr_code = dto.dict()["qr_code"]
    db_user = db.query(User).filter(User.token == token).one_or_none()
    db_umb = db.query(Umbrella).filter(Umbrella.qr_code == qr_code).one_or_none()
    if db_user is not None and db_umb is not None:
        db_umb.user_id = db_user.user_id
        image_array = np.array(dto.image, dtype=np.uint8)  # uint8list 이미지 배열 생성
        image = Image.fromarray(image_array)  # uint8list 이미지 배열을 이미지 객체로 변환
        image_byte_array = image.tobytes()  # 이미지 객체를 바이트 배열로 변환
        filename = f"image{db_umb.umb_id}.jpg"
        with open(os.path.join(ROOT_CTX, "data", "images", filename), "wb") as f:  # 바이트 배열을 로컬 파일로 저장
            f.write(image_byte_array)
        result = detect_fine_umb(filename)
        if result == "멀쩡한 우산이 있습니다.":
            db_umb.disrepair_bool = 1
            db_umb.status = "대여전"
            db_user.point += 10000
            db.commit()
            return JSONResponse(status_code=200, content=dict(msg="반납이 완료되었습니다"))
        elif result == "멀쩡한 우산이 없습니다.":
            db_umb.disrepair_bool = 0
            db_umb.status = "대여불가"
            db.commit()
            return JSONResponse(status_code=200, content=dict(msg="우산 파손으로 반납이 불가합니다"))
        else:
            return JSONResponse(status_code=200, content=dict(msg="우산 인식에 실패했습니다"))
    else:
        return JSONResponse(status_code=200, content=dict(msg="회원정보 혹은 우산 정보가 일치하지 않습니다"))


@router.post("/userinfo")
async def get_user_info(token: str = Header(None), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.token == token).first()
    if db_user is not None:
        return JSONResponse(status_code=200,
                            content=dict(user_app_id=db_user.user_app_id, name=db_user.name, point=db_user.point,
                                         created_at=str(db_user.created_at)))
    else:
        return JSONResponse(status_code=200, content=dict(msg="일치하는 회원정보가 없습니다"))