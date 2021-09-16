# -*- coding: utf-8 -*-

"""Методы обработки.
"""
from datetime import datetime, timedelta

from flask import request, jsonify

from news_api.models import NewsModel


def get_news():
    """Получить новости из БД.
    """
    day = request.args.get('day')
    news = NewsModel.query.order_by(NewsModel.news_id)
    if day:
        now = datetime.now()
        days = int(day) - 1
        last_date = now - timedelta(days=days)
        last_date = last_date.replace(hour=0, minute=0, second=0, microsecond=0)
        news = news.filter(NewsModel.date >= last_date)

    news = news.all()

    return jsonify([x.as_dict for x in news])
