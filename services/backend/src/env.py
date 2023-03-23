import os

import pymysql
from sqlalchemy import create_engine

HOSTNAME = ""
USERNAME = ""
PASSWORD = ""

PORT = 3306
DATABASE = 'bsdb'
CHARSET = 'utf8mb4'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, echo=True)

conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)

# 경로
ROOT_CTX = os.path.dirname(__file__)  # 백엔드 프로젝트 루트 경로 (~~~/services/backend/src)


if __name__ == '__main__':
    print(HOSTNAME)
