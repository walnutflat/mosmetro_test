# -*- coding: utf-8 -*-

"""Функции парсинга.
"""
from datetime import datetime
from typing import Optional

import requests
from bs4 import BeautifulSoup

from news_parser.config import BASE_URL

MONTHS = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}


def get_html(url: str) -> Optional[str]:
    """Получить HTML код страницы.
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        return None

    return resp.text


def parse_all_news(news_url: str, max_id: int = 0) -> list:
    """Распарсить все новости на странице, поулчаем новости с id > max_id.
    """
    html = get_html(news_url)
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    all_news = soup.findAll('div', class_='newslist__list-item')

    res = []
    for news in all_news:
        one_news_dict = parse_one_news(news)
        if one_news_dict['news_id'] <= max_id:
            break
        res.append(one_news_dict)

    return res


def parse_one_news(news: BeautifulSoup) -> dict:
    """Распарсить одну новость.
    """
    header = news.find('span', class_='newslist__text-title').text
    url_pic = news.find('img', class_='newslist__image')['src']
    url_news = news.find('a', class_='newslist__link')['href']
    date = parse_news_date(BASE_URL + url_news)
    news_id = int(url_news.split('/')[3])

    return {
        'news_id': news_id,
        'header': header,
        'url_pic': BASE_URL + url_pic,
        'url_news': BASE_URL + url_news,
        'date': date,
        'parsed_at': datetime.now(),
    }


def parse_news_date(url: str) -> Optional[str]:
    """Распарсить дату новости.
    """
    html = get_html(url)
    if not html:
        return None

    soup_news = BeautifulSoup(html, 'html.parser')
    date_news = soup_news.find('div', class_='pagetitle__content-date').text
    date_splitted = date_news.split()
    date_txt = f'{date_splitted[2]}-{MONTHS[date_splitted[1].lower()]}-{date_splitted[0]:0>2}'

    return date_txt
