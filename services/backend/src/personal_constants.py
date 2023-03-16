'''
개인 계정 정보, 경로 등을 저장하는 파일입니다.
커밋 하기 전 반드시 확인해 !!!!!개인정보 삭제!!!!!해주시고 조만간 gitignore에 추가할 예정입니다.
'''
import os.path
from enum import Enum


class PersonalConstant(Enum):
    # 개인 계정 정보
    db_hostname = "ls-2bcf411d91c0a47e5205379d00818b718d943b86.crboci3z63jc.ap-northeast-2.rds.amazonaws.com"  # AWS lightsail DB endpoint
    db_username = "dbmasteruser"  # AWS lightsail DB username
    db_password = "hayeon6772!"  # AWS lightsail DB password


# 경로
ROOT_CTX = os.path.dirname(__file__)  # 백엔드 프로젝트 루트 경로 (~~~/services/backend/src)

if __name__ == '__main__':
    print(PersonalConstant.db_hostname.value)
    print(PersonalConstant.db_username.value)
    print(PersonalConstant.db_password.value)
    print(ROOT_CTX)
    # 예를 들어 contents의 yolo 폴더의 best_lee.pt의 경로를 가져오고 싶다면 아래와 같이 사용
    print(os.path.join(ROOT_CTX, 'contents', 'yolo', 'best_lee.pt'))

