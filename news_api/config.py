# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

DB_NAME = os.getenv('DB_NAME')
if not DB_NAME:
    DB_NAME = 'postgresql://postgres:123456@localhost:5432/postgres'

if os.name == 'nt':
    HOST = '127.0.0.1'
else:
    HOST = '0.0.0.0'
