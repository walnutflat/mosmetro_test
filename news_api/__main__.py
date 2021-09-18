# -*- coding: utf-8 -*-

"""API для получения новостей из БД. Точка входа.
"""

from flask import Flask

from news_api.config import DB_NAME, HOST, PORT, APP_MODE
from news_api.methods import get_news
from news_api.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True


db.init_app(app)
app.add_url_rule('/metro/news', 'news', get_news)

if __name__ == '__main__':
    if APP_MODE != 'production':
        from waitress import serve
        import logging

        logger = logging.getLogger('waitress')
        logger.setLevel(logging.DEBUG)
        serve(app, host=HOST, port=PORT)
    else:
        app.run(host=HOST, debug=True)
