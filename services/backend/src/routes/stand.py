from fastapi import APIRouter, Depends, Header
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from src.cruds.stand import StandCrud
from src.database import get_db
from src.schemas.stand import StandDTO
from src.utils.tools import paging

router = APIRouter()


@router.post("/register", status_code=201)
async def register_stand(dto: StandDTO, db: Session = Depends(get_db), token: str = Header(None)):
    stand_crud = StandCrud(db, token)
    message = stand_crud.add_stand(request_stand=dto)
    return JSONResponse(content=dict(msg=message))


@router.put("/modify")
async def modify_stand(dto: StandDTO, db: Session = Depends(get_db), token: str = Header(None)):
    stand_crud = StandCrud(db, token)
    message = stand_crud.update_stand(request_stand=dto)
    return JSONResponse(content=dict(msg=message))


@router.delete("/delete/{stand_id}", status_code=200)
async def remove_stand(stand_id: int, db: Session = Depends(get_db), token: str = Header(None)):
    stand_crud = StandCrud(db, token)
    message = stand_crud.delete_stand(stand_id=stand_id)
    return JSONResponse(content=dict(msg=message))


@router.get("/page/{page}", status_code=200)
async def get_all_stands(page: int, db: Session = Depends(get_db), token: str = Header(None)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = StandCrud(db, token).fina_all_stands()
    stand_info = paginate(results, params)
    count = stand_info.dict()['total']
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info, "stand_info": stand_info}
    return JSONResponse(content=jsonable_encoder(dc))


@router.get('/page/detail/{stand_id}', status_code=200)
async def get_stand_by_id(stand_id: int, db: Session = Depends(get_db), token: str = Header(None)):
    stand_crud = StandCrud(db, token)
    stand_info = stand_crud.find_stand_by_id(stand_id=stand_id)
    return JSONResponse(content=jsonable_encoder(stand_info))
