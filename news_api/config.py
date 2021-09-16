# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

DB_NAME = 'postgresql://postgres:123456@localhost:5432/postgres'

if os.name == 'nt':
    LOG_DIR = 'D:\\'
else:
    LOG_DIR = '/home/logs/'

LOG_FILENAME = 'api.log'
LOG_FILE = os.path.join(LOG_DIR, LOG_FILENAME)
