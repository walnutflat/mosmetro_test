# -*- coding: utf-8 -*-

"""Конфигурация.
"""
import os

DB_NAME_DRAFT = 'postgresql://postgres:123456@{host}:5432/postgres'

if os.name == 'nt':
    HOST = '127.0.0.1'
    DB_NAME = DB_NAME_DRAFT.format(host='localhost')
else:
    HOST = '0.0.0.0'
    DB_NAME = DB_NAME_DRAFT.format(host='host.docker.internal')
