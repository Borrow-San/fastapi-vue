FROM python:3.9

RUN mkdir app
WORKDIR /app

RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]