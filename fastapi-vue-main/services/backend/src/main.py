import os
import sys
from fastapi_sqlalchemy.middleware import DBSessionMiddleware
from .database import init_db
from .env import DB_url
from .utils.tools import currentTime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter
from .routes.user import router as user_router
from .routes.admin import router as admin_router
from .routes.article import router as article_router
from .routes.umbrella import router as umbrella_router
from .routes.stand import router as stand_router
from .routes.rent import router as rent_router

print(f" ################ app.main Started At {currentTime()} ################# ")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(admin_router, prefix="/admins", tags=["admins"])
router.include_router(article_router, prefix="/articles", tags=["articles"])
router.include_router(umbrella_router, prefix="/umbrellas", tags=["umbrellas"])
router.include_router(stand_router, prefix="/stands", tags=["stands"])
router.include_router(rent_router, prefix="/rents", tags=["rents"])

app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_url)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {"message ": " Welcome BorrowSan !!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}