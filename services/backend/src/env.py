import pymysql
from sqlalchemy import create_engine
import os.path

ROOT_CTX = os.path.dirname(__file__)  # Backend 루트 경로 (/src)

# CORS 허용 도메인
origins = [
    "http://phayeon.site",
    "http://www.phayeon.site"
]

HOSTNAME = "ls-2bcf411d91c0a47e5205379d00818b718d943b86.crboci3z63jc.ap-northeast-2.rds.amazonaws.com"
USERNAME = "dbmasteruser"
PASSWORD = "aiFVsYKmr^=1*hUM}gncWL11Lsi;Tmo>"

PORT = 3306
DATABASE = 'bsdb'
CHARSET = 'utf8mb4'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, echo=True)
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)

OPENAI_API_KEY = "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"
