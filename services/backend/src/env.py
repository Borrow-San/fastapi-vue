import pymysql
from sqlalchemy import create_engine

HOSTNAME = "ls-2bcf411d91c0a47e5205379d00818b718d943b86.crboci3z63jc.ap-northeast-2.rds.amazonaws.com"
USERNAME = "dbmasteruser"
PASSWORD = "hayeon6772!"
PORT = 3306
DATABASE = 'bsdb'
CHARSET = 'utf8mb4'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, echo=True)
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)


if __name__ == '__main__':
    print(HOSTNAME)
