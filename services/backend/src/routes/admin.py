from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from src.cruds.admin import AdminCrud
from src.database import get_db
from src.schemas.admin import AdminDTO, AdminLoginDTO, AdminCreateDTO, AdminDeleteDTO
from src.utils.tools import paging

router = APIRouter()


@router.post("/register")
async def register_admin(dto: AdminCreateDTO, db: Session = Depends(get_db), Authorization: str = Header(None)):
    admin_crud = AdminCrud(db)
    token_or_fail_message = admin_crud.add_admin(request_admin=dto, token=Authorization)
    if "FAILURE" in token_or_fail_message:
        raise HTTPException(status_code=400, detail=token_or_fail_message)
    else:
        return JSONResponse(
            status_code=201,
            content=dict(msg=token_or_fail_message),
            media_type="application/json; charset=utf-8"
        )


@router.post("/login")
async def login_admin(dto: AdminLoginDTO, db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    token_or_fail_message = admin_crud.login(request_admin=dto)
    if "FAILURE" in token_or_fail_message:
        raise HTTPException(status_code=400, detail=token_or_fail_message)
    else:
        return JSONResponse(
            status_code=200,
            content=dict(msg=token_or_fail_message),
            media_type="application/json; charset=utf-8"
        )


@router.post("/logout")
async def logout_admin(db: Session = Depends(get_db), Authorization: str = Header(None)):
    admin_crud = AdminCrud(db)
    token_or_fail_message = admin_crud.logout(token=Authorization)
    if "FAILURE" in token_or_fail_message:
        raise HTTPException(status_code=400, detail=token_or_fail_message)
    else:
        return JSONResponse(
            status_code=200,
            content=dict(msg=token_or_fail_message),
            media_type="application/json; charset=utf-8"
        )


@router.delete("/delete")
async def remove_admin(dto: AdminDeleteDTO, db: Session = Depends(get_db), Authorization: str = Header(None)):
    admin_crud = AdminCrud(db)
    token_or_fail_message = admin_crud.delete_admin(request_admin=dto, token=Authorization)
    if "FAILURE" in token_or_fail_message:
        raise HTTPException(status_code=400, detail=token_or_fail_message)
    else:
        return JSONResponse(
            status_code=200,
            content=dict(msg=token_or_fail_message),
            media_type="application/json; charset=utf-8"
        )


@router.post("/info")
async def information_admin(db: Session = Depends(get_db), Authorization: str = Header(None)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            AdminCrud(db).find_admin_by_token(token=Authorization)))


@router.put("/new-password", status_code=200)
async def new_password(dto: AdminDTO, db: Session = Depends(get_db), Authorization: str = Header(None)):
    admin_crud = AdminCrud(db)
    message = admin_crud.update_password(request_admin=dto, token=Authorization)
    return JSONResponse(content=dict(msg=message))


@router.get("/page/{page}")
async def get_all_admins_per_page(page: int, db: Session = Depends(get_db), Authorization: str = Header(None)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = AdminCrud(db).find_all_admins_ordered(token=Authorization)
    admin_info = paginate(results, params)
    count = admin_info.dict()['total']
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info,
          "user_info": admin_info}
    return JSONResponse(status_code=200, content=jsonable_encoder(dc))


@router.get("/admin-info/{admin_id}", status_code=200)
async def get_admin(admin_id: str, db: Session = Depends(get_db), Authorization: str = Header(None)):
    admin_crud = AdminCrud(db)
    result = admin_crud.find_admin_by_id(admin_id, Authorization)
    return JSONResponse(content=jsonable_encoder(result))

