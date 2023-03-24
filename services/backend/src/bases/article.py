from abc import abstractmethod, ABCMeta
from typing import List

from src.models.article import Article
from src.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):

    @abstractmethod
    def add_article(self, request_article: ArticleDTO): pass

    @abstractmethod
    def delete_article(self, request_user: ArticleDTO): pass

    @abstractmethod
    def update_article(self, request_user: ArticleDTO): pass

    @abstractmethod
    def find_all_articles(self) -> List[Article]: pass

    @abstractmethod
    def find_articles_by_admin(self, admin_id: str) -> List[Article]: pass

    @abstractmethod
    def find_articles_by_title(self, title: str) -> List[Article]: pass
