from datetime import timezone, datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.contents.yolo.detect_fine_umb import detect_fine_umb
from src.database import get_db
from src.models.rent import Rent
from src.models.umbrella import Umbrella
from src.models.user import User
from src.schemas.flutter import TestDTO
from src.schemas.flutter import rentDTO, returnDTO

router = APIRouter()


@router.post("/rent")
async def rent_umb(dto: rentDTO, db: Session = Depends(get_db)):
    print("### 대여 라우터 진입 ### ")
    token = dto.dict()["token"]
    qr_code = dto.dict()["qr_code"]
    db_user = db.query(User).filter(User.token == token).one_or_none()

    # 수정할 부분
    if qr_code == "바로우산":
        tem_qr_code = "hfHjzBWoG485MLHbr3Epqj"
    else:
        tem_qr_code = ""

    db_umb = db.query(Umbrella).filter(Umbrella.qr_code == tem_qr_code).one_or_none()
    if db_user is not None and db_umb is not None:
        print("### 회원, 우산 정보 확인 성공 ### ")
        db_rent = Rent(user_id=db_user.user_id, umb_id=db_umb.umb_id, disrepair=1,
                       rent_time=datetime.now(timezone('Asia/Seoul')))
        db.add(db_rent)
        db_umb.status = "대여중"
        db_user.point -= 11000
        db.commit()
        return {"message": "대여 성공"}
    else:
        return {"message": "대여 실패"}


@router.post("/return")
async def return_umb(dto: returnDTO, db: Session = Depends(get_db)):
    print("### 반납 라우터 진입 ### ")

    token = dto.dict()["token"]
    qr_code = dto.dict()["qr_code"]
    image = dto.dict()["image"]
    print("##### type of image : ", type(image))

    db_user = db.query(User).filter(User.token == token).one_or_none()
    db_umb = db.query(Umbrella).filter(Umbrella.qr_code == qr_code).one_or_none()
    if db_user is not None and db_umb is not None:
        db_umb.user_id = db_user.user_id
        filename = image.filename
        content = await image.read()
        result = detect_fine_umb(filename, content)
        if result == "멀쩡한 우산이 있습니다.":
            db_umb.disrepair_bool = 1
            db_umb.status = "대여전"
            db.commit()
            return {"data": "반납이 완료되었습니다"}
        else:
            db_umb.disrepair_bool = 0
            db_umb.status = "대여불가"
            db.commit()
            return {"data": "우산 파손으로 반납이 불가합니다"}
    else:
        return {"data": "회원정보 혹은 우산 정보가 일치하지 않습니다"}


import boto3

BUCKET_NAME = 'bucket-aiacademy'
REGION_NAME = 'ap-northeast-2'
BUCKET_URL = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/borrowsan"
ACCESS_KEY = 'AKIA4FKKSBCF4BW3KPNG'
SECRET_KEY = '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'

@router.post("/test")
async def create_file(dto: TestDTO):
    image_data = bytes(dto.image)
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    print("### 1 ###")
    #s3.put_object(Bucket=BUCKET_NAME, Key="upload_test.jpg", Body=image_data)
    s3.upload_fileobj(image_data, BUCKET_NAME, "upload_test.jpg")
    print("### 2 ###")
    return {"result": "success"}
