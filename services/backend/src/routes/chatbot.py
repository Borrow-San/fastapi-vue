from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.contents.chatbot.chat_test import chat_test
from src.schemas.chatbot import ChatDTO

router = APIRouter()


@router.post("/")
async def chatbot_test(dto: ChatDTO):
    message = dto.dict()["message"]
    print(f"##### message : {message} ##### ")
    print(f"##### message type : {type(message)} ##### ")
    response = chat_test(message)
    print(f"##### response : {response} ##### ")
    dict = {"response": response}
    return JSONResponse(content=dict, status_code=200)