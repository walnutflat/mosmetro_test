# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

NEWS_URL = "https://mosmetro.ru/press/news/"
BASE_URL = "https://mosmetro.ru"

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASSWORD = '123456'
DB_NAME = 'postgres'

if os.name == 'nt':
    LOG_DIR = 'D:\\'
else:
    LOG_DIR = '/home/logs/'

LOG_FILENAME = 'parser.log'
LOG_FILE = os.path.join(LOG_DIR, LOG_FILENAME)
