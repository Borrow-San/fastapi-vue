from fastapi import APIRouter, Depends, Header
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from src.cruds.rent import RentCrud
from src.database import get_db
from src.schemas.rent import RentDTO
from src.utils.tools import paging

router = APIRouter()


@router.post("/register", status_code=201)
async def register_rent(dto: RentDTO, db: Session = Depends(get_db), token: str = Header(None)):
    rent_crud = RentCrud(db, token)
    message = rent_crud.add_rent(request_rent=dto)
    return JSONResponse(content=dict(msg=message))


@router.put("/modify")
async def modify_rent(dto: RentDTO, db: Session = Depends(get_db), token: str = Header(None)):
    rent_crud = RentCrud(db, token)
    message = rent_crud.update_rent(request_rent=dto)
    return JSONResponse(content=dict(msg=message))


@router.delete("/delete/{rent_id}", status_code=200)
async def remove_rent(rent_id: int, db: Session = Depends(get_db), token: str = Header(None)):
    rent_crud = RentCrud(db, token)
    message = rent_crud.delete_rent(rent_id=rent_id)
    return JSONResponse(content=dict(msg=message))


@router.get("/page/{page}", status_code=200)
async def get_all_rents(page: int, db: Session = Depends(get_db), token: str = Header(None)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = RentCrud(db, token).fina_all_rents()
    rent_info = paginate(results, params)
    count = rent_info.dict()['total']
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info, "rent_info": rent_info}
    return JSONResponse(content=jsonable_encoder(dc))


@router.get('/page/detail/{rent_id}', status_code=200)
async def get_rent_by_id(rent_id: int, db: Session = Depends(get_db), token: str = Header(None)):
    rent_crud = RentCrud(db, token)
    rent_info = rent_crud.find_rent_by_id(rent_id=rent_id)
    return JSONResponse(content=jsonable_encoder(rent_info))
