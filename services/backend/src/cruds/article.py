from abc import ABC
from typing import List, Any, Union, Dict
import pymysql
from sqlalchemy.orm import Session
from src.bases.article import ArticleBase
from src.models.article import Article
from src.schemas.article import ArticleDTO, ArticleCreateDTO, ArticleSearchDTO, ArticleDeleteDTO

from src.models.admin import Admin
from src.utils.security import match_token
from src.utils.util_aws import upload_to_aws

pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):
    def __init__(self, db: Session, token: str):
        self.db: Session = db
        self.auth = match_token(db=db, token=token, db_model=Admin)

    def add_article(self, request_article: ArticleCreateDTO) -> str:
        if self.auth:
            article = Article(**request_article.dict())
            article.admin_id = self.auth.admin_id
            self.db.add(article)
            self.db.commit()
            return "SUCCESS: 게시물 생성 완료"
        else:
            return "FAILURE: 게시물 생성 실패"

    def upload_file(self, file) -> str:
        if self.auth:
            file_location = file.filename
            file_url = upload_to_aws(file.file, file_location)
            return file_url
        else:
            return "FAILURE: 이미지 업로드 실패"

    def delete_article(self, request_article: ArticleSearchDTO) -> str:
        if self.auth:
            articles = self.find_article_by_option(request_article, option=request_article.option)
            if articles:
                for article in articles:
                    self.db.delete(article)
                self.db.commit()
                return "SUCCESS: 게시물 삭제 완료"
            else:
                return "FAILURE: 해당 게시물이 존재하지 않습니다."
        else:
            return "FAILURE: 게시물 삭제 실패"

    def update_article(self, request_article: ArticleDTO) -> str:
        is_success = self.db.query(Article).\
            filter(Article.article_id == request_article.article_id). \
            update(request_article.dict(exclude_unset=True)
                   , synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "업데이트 실패"

    def find_all_articles(self) -> List[Article]:
        return self.db.query(Article).all()

    def find_article_by_option(self, request_article: ArticleSearchDTO, option: str) -> Article:
        return self.db.query(Article).filter(getattr(Article, option) == getattr(request_article, option)).all()
