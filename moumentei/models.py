__author__ = 'peter'

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from datetime import datetime
from sqlalchemy.dialects import postgresql

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))


class Article(DeclarativeBase):
    """Sqlalchemy articles model"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    author = Column(String)
    content = Column(String, nullable=True)
    segmented = Column(postgresql.ARRAY(String), nullable=True)
    url = Column(String, nullable=True)
    like = Column(Integer, nullable=True)
    dislike = Column(Integer, nullable=True)
    published_at = Column(DateTime, nullable=True)
