# -*- coding: utf-8 -*-

"""Модели.
"""
from sqlalchemy import create_engine, Column, Date, String, Text, Integer, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

from news_parser.config import DB_NAME, SQL_ECHO

engine = create_engine(DB_NAME, echo=SQL_ECHO)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class NewsModel(Base):
    """Модель записи новости.
    """
    __tablename__ = 'metro_news'

    news_id = Column(Integer, primary_key=True, nullable=False)
    header = Column(Text(), nullable=True)
    url_pic = Column(String(), nullable=True)
    url_news = Column(String(), nullable=True)
    date = Column(Date(), nullable=True)
    parsed_at = Column(DateTime())
