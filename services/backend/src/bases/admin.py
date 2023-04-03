from abc import abstractmethod, ABCMeta
from typing import List
from src.models.admin import Admin
from src.schemas.admin import AdminDTO


class LoginBase(metaclass=ABCMeta):

    @abstractmethod
    def login(self, request_admin: AdminDTO) -> str: pass

    @abstractmethod
    def update_token(self, db_admin: Admin, new_token: str) -> str: pass


class AdminBase(metaclass=ABCMeta):

    @abstractmethod
    def add_admin(self, request_admin: AdminDTO) -> str: pass

    @abstractmethod
    def logout(self, request_admin: AdminDTO) -> str: pass

    @abstractmethod
    def update_password(self, request_admin: AdminDTO) -> str: pass

    @abstractmethod
    def delete_admin(self, request_admin: AdminDTO) -> str: pass

    @abstractmethod
    def find_all_admins_ordered(self) -> List[Admin]: pass

    @abstractmethod
    def find_all_admins(self) -> List[Admin]: pass
