# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

NEWS_URL = "https://mosmetro.ru/press/news/"
BASE_URL = "https://mosmetro.ru"

DB_NAME_DRAFT = 'postgresql://postgres:123456@{host}:5432/postgres'


if os.name == 'nt':
    LOG_DIR = 'D:\\'
    DB_NAME = DB_NAME_DRAFT.format(host='localhost')
else:
    LOG_DIR = '/home/logs/'
    DB_NAME = DB_NAME_DRAFT.format(host='host.docker.internal')

LOG_FILENAME = 'parser.log'
LOG_FILE = os.path.join(LOG_DIR, LOG_FILENAME)

SQL_ECHO = False
SLEEP_MINUTES = 10