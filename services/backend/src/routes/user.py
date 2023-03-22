from datetime import timezone, datetime

from fastapi import APIRouter, Depends, Header
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from src.contents.yolo.detect_fine_umb import detect_fine_umb
from src.cruds.user import UserCrud
from src.database import get_db
from src.models.rent import Rent
from src.models.umbrella import Umbrella
from src.models.user import User
from src.schemas.rent import RentDTOdata
from src.schemas.user import UserDTO, UserUpdate
from src.utils.tools import paging

router = APIRouter()


@router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(content=dict(
                            msg=UserCrud(db).add_user(request_user=dto)))


@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    token_or_fail_message = user_crud.login(request_user=dto)
    return JSONResponse(content=dict(msg=token_or_fail_message))


@router.post("/logout", status_code=200)
async def logout_user(token: str = Header(None), db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    token_or_fail_message = user_crud.logout(token=token)
    return JSONResponse(content=dict(msg=token_or_fail_message))


@router.post("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):

        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/modify")
async def modify_user(dto: UserUpdate, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).update_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/new-password")
async def new_password(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).update_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.delete("/delete", tags=['age'])
async def remove_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    message = user_crud.delete_user(dto)
    return JSONResponse(status_code=400, content=dict(msg=message))


@router.get("/page/{page}", response_model=Page[UserDTO])
async def get_all_users_per_page(page: int, db: Session = Depends(get_db)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = UserCrud(db).find_all_users_ordered()
    user_info = paginate(results, params)
    count = UserCrud(db).count_all_users()
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info,
          "user_info": user_info}
    return JSONResponse(status_code=200, content=jsonable_encoder(dc))


@router.get("/page/{page}/size/{size}", response_model=Page[UserDTO])
async def get_all_users_per_page_with_size(page: int, size: int, db: Session = Depends(get_db)):
    params = Params(page=page, size=size)
    results = UserCrud(db).find_all_users_ordered()
    page_result = paginate(results, params)
    return JSONResponse(status_code=200, content=jsonable_encoder(page_result))


@router.get("/list")
async def get_all_users(db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    ls = user_crud.find_all_users()
    return {"data": ls}


@router.get("/id/{id}")
async def get_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    result = user_crud.find_user_by_id(dto)
    return result


@router.get("/email/{email}/page/{page}")
async def get_userid_by_email(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.find_user_by_email(dto)
    return {"data": "success"}

@router.post("/rent")
async def rent_umb(dto: RentDTOdata, db: Session = Depends(get_db)):
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
        db_rent = Rent(user_id=db_user.user_id, umb_id=db_umb.umb_id, disrepair=1, rent_time=datetime.now(timezone('Asia/Seoul')))
        db.add(db_rent)
        db_umb.status = "대여중"
        db_user.point -= 11000
        db.commit()
        return {"message": "대여 성공"}
    else:
        return {"message": "대여 실패"}


@router.post("/return")
async def return_umb(dto: RentDTOdata, db: Session = Depends(get_db)):
    token = dto.dict()["token"]
    qr_code = dto.dict()["qr_code"]
    image = dto.dict()["image"]
    db_user = db.query(User).filter(User.token == token).one_or_none()
    db_umb = db.query(Umbrella).filter(Umbrella.qr_code == qr_code).one_or_none()
    if db_user is not None and db_umb is not None:
        db_umb.user_id = db_user.user_id
        filename = image.filename
        content = await image.read()
        result = detect_fine_umb(filename, content)
        if result == "멀쩡한 우산이 있습니다.":
            db_umb.disrepair_bool = 1
            db_umb.status = "대여중"
            db.commit()
            return {"data": "success"}
