from fastapi import APIRouter, Depends, Header
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from src.cruds.umbrella import UmbrellaCrud
from src.database import get_db
from src.schemas.umbrella import UmbrellaDTO
from src.utils.tools import paging

router = APIRouter()


@router.post("/register", status_code=201)
async def register_umbrella(dto: UmbrellaDTO, db: Session = Depends(get_db), token: str = Header(None)):
    umbrella_crud = UmbrellaCrud(db, token)
    message = umbrella_crud.add_umbrella(request_umbrella=dto)
    return JSONResponse(content=dict(msg=message))


@router.put("/modify")
async def modify_umbrella(dto: UmbrellaDTO, db: Session = Depends(get_db), token: str = Header(None)):
    umbrella_crud = UmbrellaCrud(db, token)
    message = umbrella_crud.update_umbrella(request_umbrella=dto)
    return JSONResponse(content=dict(msg=message))


@router.delete("/delete/{umb_id}", status_code=200)
async def remove_umbrella(umb_id: int, db: Session = Depends(get_db), token: str = Header(None)):
    umbrella_crud = UmbrellaCrud(db, token)
    message = umbrella_crud.delete_umbrella(umb_id=umb_id)
    return JSONResponse(content=dict(msg=message))


@router.get("/page/{page}", status_code=200)
async def get_all_umbrellas(page: int, db: Session = Depends(get_db), token: str = Header(None)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = UmbrellaCrud(db, token).find_all_umbrellas()
    umbrella_info = paginate(results, params)
    count = umbrella_info.dict()['total']
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info, "umbrella_info": umbrella_info}
    return JSONResponse(content=jsonable_encoder(dc))


@router.get('/page/detail/{umb_id}', status_code=200)
async def get_umbrella_by_id(umb_id: int, db: Session = Depends(get_db), token: str = Header(None)):
    umbrella_crud = UmbrellaCrud(db, token)
    umb_info = umbrella_crud.find_umbrella_by_id(umb_id=umb_id)
    return JSONResponse(content=jsonable_encoder(umb_info))
