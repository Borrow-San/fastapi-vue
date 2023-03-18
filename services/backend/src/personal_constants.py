'''
개인 계정 정보, 경로 등을 저장하는 파일입니다.
깃 커밋 시 반드시 확인 해주시고 조만간 gitignore에 추가할 예정입니다.
'''
import os.path
from enum import Enum

# 경로
ROOT_CTX = os.path.dirname(__file__)  # 백엔드 프로젝트 루트 경로


def dir_path(keyword):  # 프로젝트 src 하위 경로 ex) dir_path("test") -> ~~~/backend/src/test
    return os.path.join(ROOT_CTX, "", keyword)

