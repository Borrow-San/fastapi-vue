from fastapi import APIRouter
from src.schemas.chatbot import ChatDTO
from starlette.responses import JSONResponse
import openai

router = APIRouter()

openai.api_key = ""

prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, " \
         "I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, " \
         "I will respond with \"Unknown\".\n\n" \
         "Q: What is human life expectancy in the United States?\n" \
         "A: Human life expectancy in the United States is 78 years.\n\n" \
         "Q: Who was president of the United States in 1955?\n" \
         "A: Dwight D. Eisenhower was president of the United States in 1955.\n\n" \
         "Q: Which party did he belong to?\n" \
         "A: He belonged to the Republican Party.\n\n" \
         "Q: What is the square root of banana?\n" \
         "A: Unknown\n\n" \
         "Q: How does a telescope work?\n" \
         "A: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\n" \
         "Q: Where were the 1992 Olympics held?\n" \
         "A: The 1992 Olympics were held in Barcelona, Spain.\n\n" \
         "Q: How many squigs are in a bonk?\n" \
         "A: Unknown\n\n" \
         "Q: 이거 뭐하는 어플이야?\n" \
         "A: 우산을 빌려주는 어플입니다\n\n" \
         "Q: 무슨 어플이야?\n" \
         "A: 우산 빌려드려요\n\n" \
         "Q: 이거 뭔데\n" \
         "A: 우산을 빌려드려요\n\n"


@router.post("/gpt3")
async def chatbot_gpt3(dto: ChatDTO):
    message = dto.dict()["message"]
    question = message
    response = (openai.Completion()).create(
        engine="text-davinci-003",
        prompt=prompt + question,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1,
    )
    answer = response.choices[0].text.strip()
    return JSONResponse(content={"response": answer}, status_code=200)
