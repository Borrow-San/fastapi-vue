import pymysql
from sqlalchemy import create_engine
import os.path

ROOT_CTX = os.path.dirname(__file__)  # Backend 루트 경로 (/src)

# CORS 허용 도메인
origins = [
    "http://phayeon.site",
    "http://www.phayeon.site"
]

BUCKET_NAME = ""
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""


PORT = 3306
DATABASE = 'bsdb'
CHARSET = 'utf8mb4'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, echo=True)
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)

OPENAI_API_KEY = ""
