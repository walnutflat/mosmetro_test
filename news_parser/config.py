# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

NEWS_URL = "https://mosmetro.ru/press/news/"
BASE_URL = "https://mosmetro.ru"

DB_NAME = 'postgresql://postgres:123456@localhost:5432/postgres'


if os.name == 'nt':
    LOG_DIR = 'D:\\'
else:
    LOG_DIR = '/home/logs/'

LOG_FILENAME = 'parser.log'
LOG_FILE = os.path.join(LOG_DIR, LOG_FILENAME)

SQL_ECHO = False
