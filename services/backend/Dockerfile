FROM python:3.9

RUN mkdir app
WORKDIR /app

RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx
<<<<<<< HEAD

COPY requirements.txt .
=======
COPY ./requirements.txt ./
>>>>>>> fe1afd13291d1781761b2e1bdcadd9c6697bafbc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]