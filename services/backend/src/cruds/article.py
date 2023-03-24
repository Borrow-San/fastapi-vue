from abc import ABC
from typing import List
import pymysql
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.bases.article import ArticleBase
from src.models.article import Article
from src.models.user import User
from src.schemas.article import ArticleDTO

from src.models.admin import Admin

pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):
    def __init__(self, db: Session, token: str):
        self.db: Session = db
        self.admin = self.db.query(Admin).filter(Admin.token == token).first()
        if not self.admin:
            raise HTTPException(status_code=401, detail="Invalid token")

    def add_article(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        if article:
            article.admin_id = self.admin.admin_id
            self.db.add(article)
            self.db.commit()
            return "success"
        else:
            return ""

    def delete_article(self, request_article: ArticleDTO) -> str:
        article = self.find_article_by_article_id(request_article)
        if article:
            self.db.delete(article)
            self.db.commit()
            message = "SUCCESS: 게시물 삭제 완료"
        else:
            message = "FAILURE: 게시물 삭제 실패"
        return message

    def update_article(self, request_article: ArticleDTO) -> str:
        is_success = self.db.query(Article).\
            filter(Article.article_id == request_article.article_id). \
            update(request_article.dict(exclude_unset=True)
                   , synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "업데이트 실패"

    def find_all_articles(self) -> List[Article]:
        return self.db.query(Article).all()

    def find_articles_by_admin(self, admin_id: str) -> List[Article]:
        return self.db.query(Article).filter(Article.admin_id == admin_id).all()

    def find_articles_by_title(self, title: str) -> List[Article]:
        return self.db.query(Article).filter(Article.title == title).all()

    def find_article_by_article_id(self, request_article: ArticleDTO) -> Article:
        return self.db.query(Article).filter(Article.article_id == request_article.article_id).first()
