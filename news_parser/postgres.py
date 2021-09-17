# -*- coding: utf-8 -*-

"""Функции для работы с БД.
"""

from typing import Optional

from sqlalchemy import func

from news_parser.models import NewsModel


def get_last_id(session) -> Optional[int]:
    """Получить id последней новости.
    """
    max_id = session.query(func.max(NewsModel.news_id))[0]
    if max_id is None:
        return None

    return max_id[0] or 0


def save_news(logger, session, all_news: list) -> Optional[int]:
    """Сохранить список новостей в БД.
    """
    # noinspection PyBroadException
    try:
        for news in all_news:
            new_news = NewsModel(**news)
            session.add(new_news)

        session.commit()
    except Exception as exc:
        logger.error(exc)
        return 0

    return len(all_news)





