# -*- coding: utf-8 -*-

"""Парсер новостей. Точка входа.
"""
from loguru import logger

from news_parser.config import NEWS_URL, LOG_FILE
from news_parser.models import Session, engine
from news_parser.parsing import parse_all_news
from news_parser.postgres import get_last_id, save_news


@logger.catch
def main():
    logger.add(LOG_FILE)
    logger.warning('Старт парсера новостей')

    session = Session()

    try:
        max_id = get_last_id(session)
        logger.info(f'Получен id последней новости = {max_id}')

        all_news = parse_all_news(NEWS_URL, max_id)
        logger.info(f'Получено {len(all_news)} новостей с сайта')

        if all_news:
            count = save_news(logger, session, all_news)
            logger.info(f'Сохранено {count} новостей с сайта')

    finally:
        engine.dispose()
        logger.warning('Остановка парсера новостей')


if __name__ == '__main__':
    main()
