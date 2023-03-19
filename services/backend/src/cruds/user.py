from abc import ABC
from typing import List
import pymysql
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.bases.user import UserBase
from src.models.user import User
from src.schemas.user import UserDTO, UserUpdate
from src.utils.security import myuuid, get_hashed_password, verify_password, generate_token

pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user_dict = User(**request_user.dict())
        if self.find_user_by_email(request_user=request_user) is None:
            user_dict.user_id = myuuid()
            user_dict.password = get_hashed_password(user_dict.password)
            is_success = self.db.add(user_dict)
            self.db.commit()
            self.db.refresh(user_dict)
            message = "SUCCESS: 회원가입이 완료되었습니다" if is_success != 0 else "FAILURE: 회원가입이 실패하였습니다"
        else:
            message = "FAILURE: 아이디가 이미 존재합니다"
        return message

    def login(self, request_user: UserDTO) -> str:
        user_email = self.db.query(User).filter(User.email == request_user.email).one_or_none()
        if user_email is not None:
            verified = verify_password(plain_password=request_user.password,
                                       hashed_password=user_email.password)
            if verified:
                new_token = generate_token(request_user.email)
                request_user.token = new_token
                self.update_token(user_email, new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다"
        else:
            return "FAILURE: 이메일 주소가 존재하지 않습니다"

    def logout(self, token: str) -> str:
        user = self.match_token(token)
        if user:
            user.token = ""
            self.db.commit()
            return "SUCCESS"

    def update_user(self, request_user: UserUpdate) -> str:
        db_user = self.find_user_by_id_for_update(request_user)
        for var, value in vars(request_user).items():
            setattr(db_user, var, value) if value else None
        is_success = self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return "success" if is_success != 0 else "failed"

    def update_token(self, db_user: User, new_token: str) -> str:
        is_success = self.db.query(User).filter(User.user_id == db_user.user_id) \
            .update({User.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_user)
        return "success" if is_success != 0 else "failed"

    def update_password(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        user.password = get_hashed_password(user.password)
        is_success = self.db.query(User).filter(User.token == user.token) \
            .update({User.password: user.password}, synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "failed"

    def delete_user(self, request_user: UserDTO) -> str:
        user = self.find_user_by_id(request_user)
        print(f"### user is : ### \n{user}")
        is_success = self.db.query(User).filter(User.user_id == user.user_id).delete(synchronize_session=False)
        self.db.commit()
        return "탈퇴 성공입니다." if is_success != 0 else "탈퇴 실패입니다."

    def find_all_users_ordered(self) -> List[User]:
        return self.db.query(User).order_by(User.created_at).all()

    def find_user_by_token(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.token == user.token).one_or_none()

    def find_user_by_id(self, request_user: UserDTO) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.user_id == user.user_id).one_or_none()

    def find_user_by_id_for_update(self, request_user: UserUpdate) -> User:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.token == user.token).one_or_none()

    def find_user_by_email(self, request_user: UserDTO) -> None:
        return self.db.query(User).filter(User.email == request_user.email).one_or_none()

    def find_all_users(self) -> List[User]:
        return self.db.query(User).all()

    def match_token(self, token: str) -> bool:
        user = self.db.query(User).filter(User.token == token).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user

    def match_token_for_modify(self, request_user: UserUpdate) -> bool:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.token == user.token).one_or_none()
        return True if db_user != None else False

    def count_all_users(self) -> int:
        return self.db.query(User).count()
