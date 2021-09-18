# -*- coding: utf-8 -*-

"""Парсер новостей. Точка входа.
"""
from time import sleep

from loguru import logger
from sqlalchemy.exc import SQLAlchemyError

from news_parser.config import NEWS_URL, LOG_FILE, SLEEP_TO_RETRY_SEC, SLEEP_SECONDS
from news_parser.models import Session, engine
from news_parser.parsing import parse_all_news
from news_parser.postgres import get_last_id, save_news


@logger.catch
def main():
    """Точка входа.
    """
    logger.add(LOG_FILE)
    logger.warning('Старт парсера новостей')

    while True:
        retry = handle()
        sleep_time = SLEEP_TO_RETRY_SEC if retry else SLEEP_SECONDS
        logger.info(f'Ожидание {sleep_time} секунд')
        sleep(sleep_time)


def handle():
    """Основнорй обработчик.
    """
    session = Session()
    logger.info('Начало нового круга')
    retry = False

    try:
        max_id = get_last_id(session)
        logger.info(f'Получен id последней новости = {max_id}')

        all_news = parse_all_news(NEWS_URL, max_id)
        logger.info(f'Получено {len(all_news)} новостей с сайта')

        if all_news:
            count = save_news(logger, session, all_news)
            logger.info(f'Сохранено {count} новостей с сайта')

    except SQLAlchemyError as exc:
        retry = True
        logger.error(f'Ошибка БД: {exc}')

    finally:
        engine.dispose()
        logger.info('Окончание круга')
        return retry


if __name__ == '__main__':
    main()
