import os
import sys
from fastapi_sqlalchemy.middleware import DBSessionMiddleware

from src.database import init_db
from src.env import DB_url
from src.contents.yolo.yolov5_test import yolov5_test
from src.utils.tools import currentTime
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter, UploadFile

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

from src.routes.user import router as user_router
from src.routes.admin import router as admin_router
from src.routes.article import router as article_router
from src.routes.umbrella import router as umbrella_router
from src.routes.stand import router as stand_router
from src.routes.rent import router as rent_router
from src.routes.chatbot import router as chatbot_router

print(f" ################ app.main Started At {currentTime()} ################# ")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(admin_router, prefix="/admin", tags=["admin"])
router.include_router(article_router, prefix="/articles", tags=["articles"])
router.include_router(umbrella_router, prefix="/umbrellas", tags=["umbrellas"])
router.include_router(stand_router, prefix="/stands", tags=["stands"])
router.include_router(rent_router, prefix="/rents", tags=["rents"])
router.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])

app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_url)

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {"message ": " Welcome BorrowSan !!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/yolotest")
async def yolotest(file: UploadFile):
    filename = file.filename
    content = await file.read()
    result = yolov5_test(filename, content)
    return {"result": result}
