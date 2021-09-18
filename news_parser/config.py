# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

NEWS_URL = "https://mosmetro.ru/press/news/"
BASE_URL = "https://mosmetro.ru"

DB_NAME = os.getenv('DB_NAME')
if not DB_NAME:
    DB_NAME = 'postgresql://postgres:123456@localhost:5432/postgres'


if os.name == 'nt':
    LOG_DIR = 'D:\\'
else:
    LOG_DIR = '/home/logs/'

LOG_FILENAME = 'parser.log'
LOG_FILE = os.path.join(LOG_DIR, LOG_FILENAME)

SQL_ECHO = False
SLEEP_MINUTES = 10
SLEEP_TO_RETRY_SEC = 10
SLEEP_SECONDS = SLEEP_MINUTES * 60
