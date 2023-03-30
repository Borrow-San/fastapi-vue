import os
import sys

from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy.middleware import DBSessionMiddleware
from src.database import init_db
from src.env import DB_url
from src.utils.tools import currentTime
from starlette.middleware.cors import CORSMiddleware

from services.backend.src.env import engine

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
import openai

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

origins = [
    "http://localhost",
    "http://localhost:8080"
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

@app.get("chat")
async def chatbot():
    openai.api_key = "org-0fNmz2TnCxtZZqJ9xRs47Jit"

    messages = []

    while True:
        user_content = input(f"user : ")

        messages.append({"role": "user", "content": f"{user_content}"})  # 사용자의 질문을 리스트에 추가

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        gpt_content = completion.choices[0].message["content"].strip()  # 챗봇의 답변을 변수에 저장

        messages.append({"role": "assistant", "content": f"{gpt_content}"})  # 챗봇 답변을 리스트에 추가
        print(f"GPT : {gpt_content}")  # 챗봇의 답변 출력
        engine.say(gpt_content)
        engine.runAndWait()  # 답변이 끝날때 까지 대기
        engine.stop()  # 대답 출력 중지

