from abc import ABC
from typing import List
from sqlalchemy.orm import Session

from src.bases.admin import AdminBase, LoginBase
from src.models.admin import Admin
from src.schemas.admin import AdminDTO, AdminLoginDTO, AdminCreateDTO, AdminDeleteDTO
from src.utils.security import myuuid, get_hashed_password, verify_password, generate_token

from src.models.article import Article

from src.utils.security import match_token


class LoginCrud(LoginBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def login(self, request_admin: AdminLoginDTO) -> str:
        admin_id = self.db.query(Admin).filter(Admin.admin_id == request_admin.admin_id).one_or_none()
        if admin_id is not None:
            verified = verify_password(plain_password=request_admin.password,
                                       hashed_password=admin_id.password)
            if verified:
                new_token = generate_token(request_admin.name)
                request_admin.token = new_token
                self.update_token(admin_id, new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다"
        else:
            return "FAILURE: 아이디가 일치하지 않습니다"

    def update_token(self, db_admin: Admin, new_token: str) -> str:
        is_success = self.db.query(Admin).filter(Admin.admin_id == db_admin.admin_id) \
            .update({Admin.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_admin)
        return "success" if is_success != 0 else "failed"


class AdminCrud(AdminBase, ABC):
    def __init__(self, db: Session, token: str):
        self.db: Session = db
        self.token = token
        self.auth = match_token(db=db, token=token, db_model=Admin)

    def add_admin(self, request_admin: AdminCreateDTO) -> str:
        if self.auth:
            admin_name = self.find_admin_by_option(request_admin=request_admin, option="name")
            if admin_name is None:
                admin_dict = Admin(**request_admin.dict())
                admin_dict.admin_id = myuuid()
                admin_dict.password = get_hashed_password(admin_dict.password)
                is_success = self.db.add(admin_dict)
                self.db.commit()
                self.db.refresh(admin_dict)
                message = "SUCCESS: 회원가입이 완료되었습니다" if is_success != 0 else "FAILURE: 회원가입이 실패하였습니다"
            else:
                message = "FAILURE: 이름이 이미 존재합니다"
            return message

    def logout(self) -> str:
        if self.auth:
            self.auth.token = ""
            self.db.commit()
            return "SUCCESS"
        else:
            return "FAILURE: 로그아웃에 실패하였습니다."

    def delete_admin(self, request_admin: AdminDeleteDTO) -> str:
        admin_to_delete = self.find_admin_by_option(request_admin=request_admin, option="admin_id")
        if admin_to_delete is not None:
            admin_name = admin_to_delete.name
            self.db.query(Article).filter(Article.admin_id == admin_to_delete.admin_id).delete(synchronize_session=False)
            self.db.delete(admin_to_delete)
            self.db.commit()
            return f"{admin_name}님의 계정과 게시물이 삭제 되었습니다."
        else:
            return "FAILURE: 삭제 할 유저 정보를 확인 해 주세요."

    def update_password(self, request_admin: AdminDTO) -> str:
        admin = self.auth
        admin.password = get_hashed_password(request_admin.password)
        is_success = self.db.query(Admin).filter(Admin.token == admin.token) \
            .update({Admin.password: admin.password}, synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "failed"

    def find_all_admins_ordered(self) -> List[Admin]:
        if self.auth:
            return self.db.query(Admin).order_by(Admin.created_at).all()

    def find_all_admins(self) -> List[Admin]:
        return self.db.query(Admin).all()

    def find_admin_by_option(self, request_admin: List, option: str) -> Admin:
        return self.db.query(Admin).filter(getattr(Admin, option) == getattr(request_admin, option)).all()
