import os
import sys

from fastapi import FastAPI, APIRouter, WebSocket
from fastapi_sqlalchemy.middleware import DBSessionMiddleware
from src.database import init_db
from src.env import DB_url, origins
from src.utils.tools import currentTime
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketDisconnect

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

from src.routes.user import router as user_router
from src.routes.admin import router as admin_router
from src.routes.article import router as article_router
from src.routes.umbrella import router as umbrella_router
from src.routes.stand import router as stand_router
from src.routes.rent import router as rent_router
from src.routes.chatbot import router as chatbot_router
from src.routes.flutter import router as flutter_router

print(f" ################ app.main Started At {currentTime()} ################# ")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(admin_router, prefix="/admins", tags=["admins"])
router.include_router(article_router, prefix="/articles", tags=["articles"])
router.include_router(umbrella_router, prefix="/umbrellas", tags=["umbrellas"])
router.include_router(stand_router, prefix="/stands", tags=["stands"])
router.include_router(rent_router, prefix="/rents", tags=["rents"])
router.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])
router.include_router(flutter_router, prefix="/flutter", tags=["flutter"])

app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_url)


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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.get("/")
async def root():
    return {"message ": " Welcome BorrowSan !!"}
