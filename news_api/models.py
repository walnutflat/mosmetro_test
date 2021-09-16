# -*- coding: utf-8 -*-

"""Модели.
"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class NewsModel(db.Model):
    """Модель записи новости.
    """
    __tablename__ = 'metro_news'

    news_id = db.Column(db.Integer, primary_key=True, nullable=False)
    header = db.Column(db.Text(), nullable=True)
    url_pic = db.Column(db.String(), nullable=True)
    url_news = db.Column(db.String(), nullable=True)
    date = db.Column(db.Date(), nullable=True)

    def __init__(self, news_id, header, url_pic, url_news, date):
        self.news_id = news_id
        self.header = header
        self.url_pic = url_pic
        self.url_news = url_news
        self.date = date

    @property
    def as_dict(self):
        """Вернуть представление в виде словаря.
        """
        return {
            'news_id': self.news_id,
            'header': self.header,
            'url_pic': self.url_pic,
            'url_news': self.url_news,
            'date': str(self.date),
        }