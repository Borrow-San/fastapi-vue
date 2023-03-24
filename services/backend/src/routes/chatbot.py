from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.contents.chatbot.chatbot_gpt3 import chatbot_gpt3
from src.schemas.chatbot import ChatDTO

router = APIRouter()


@router.post("/gpt3")
async def chatbot(dto: ChatDTO):
    question = dto.dict()["message"]
    answer = chatbot_gpt3(question)
    return JSONResponse(content={"response": answer}, status_code=200)
