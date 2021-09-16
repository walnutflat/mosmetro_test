# -*- coding: utf-8 -*-

"""Функции для работы с БД.
"""

from typing import Optional

import psycopg2 as psycopg2
from loguru import logger
from psycopg2.extras import execute_values

from news_parser.config import DB_PASSWORD, DB_NAME, DB_USER, DB_HOST, DB_PORT


def make_connection():
    """Создать подключение и вернуть его или None.
    """
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        conn.autocommit = False
        return conn
    except Exception as exc:
        logger.error(f'Ошибка при создании подключения к {DB_HOST}: {exc}')
        return None


def execute_command(conn, query: str):
    """Выполнить запрос.
    """
    with conn.cursor() as cursor:
        # noinspection PyBroadException
        try:
            cursor.execute(query)
            conn.commit()
            return cursor.fetchone()
        except Exception as exc:
            logger.error(f'Ошибка при выполнении команды {query}: {exc}')
            return None


def get_last_id(conn) -> Optional[int]:
    """Получить id последней новости.
    """
    stmt = """
    SELECT max(news_id)
    FROM public.metro_news
    """.strip()
    max_id = execute_command(conn, stmt)
    if max_id is None:
        return None

    return max_id[0] or 0


def save_news(conn, all_news: list) -> Optional[int]:
    """Сохранить список новостей в БД.
    """
    news_tuples = [tuple(news.values()) for news in all_news]
    stmt = 'INSERT INTO public.metro_news (news_id, header, url_pic, url_news, date, parsed_at) ' \
           'VALUES %s ON CONFLICT DO NOTHING'
    with conn.cursor() as cursor:
        # noinspection PyBroadException
        try:
            execute_values(cursor, stmt, news_tuples)
            conn.commit()
            return len(news_tuples)
        except Exception as exc:
            logger.exception(exc)
            return None


