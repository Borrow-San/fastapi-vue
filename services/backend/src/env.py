import pymysql
from sqlalchemy import create_engine

from src.personal_constants import PersonalConstant

HOSTNAME = PersonalConstant.db_hostname.value
USERNAME = PersonalConstant.db_username.value
PASSWORD = PersonalConstant.db_password.value
PORT = 3306
DATABASE = 'bsdb'
CHARSET = 'utf8mb4'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, echo=True)
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)


if __name__ == '__main__':
    print(HOSTNAME)
