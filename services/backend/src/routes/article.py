from fastapi import APIRouter, Depends, Header
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi_pagination import paginate, Params
from src.cruds.article import ArticleCrud
from src.database import get_db
from src.schemas.article import ArticleDTO
from src.utils.tools import paging


router = APIRouter()


@router.post("/register", status_code=201)
async def register_article(dto: ArticleDTO, db: Session = Depends(get_db), token: str = Header(None)):
    article_crud = ArticleCrud(db)
    message = article_crud.add_article(request_article=dto, token=token)
    return JSONResponse(status_code=201, content=dict(msg=message))


@router.delete("/remove", status_code=201)
async def remove_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    message = article_crud.delete_article(request_article=dto)
    return JSONResponse(status_code=201, content=dict(msg=message))


@router.patch("/update", status_code=201)
async def update_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.update_article(request_article=dto)


@router.get("/page/{page}", status_code=201)
async def get_all_articles(page: int, db: Session = Depends(get_db)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = ArticleCrud(db).find_all_articles()
    article_info = paginate(results, params)
    count = article_info.dict()['total']
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info,
          "user_info": article_info}
    return JSONResponse(status_code=200, content=jsonable_encoder(dc))


@router.get("/id/{article_id}/page/{page}", status_code=201)
async def get_articles_by_userid(article_id: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_userid(article_id=article_id)


@router.get("/title/{title}/page/{page}", status_code=201)
async def get_articles_by_title(title: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_title(title=title)
