# mosmetro_test
Сервис по парсингу новостей с сайта московского метро в БД + API, по которому эти новости можно получить

### Модуль news_parser
Парсит сайт метро и записывает их в БД через ORM. Работает в бесконечном цикле. C beautifulsoup не работал, лучшие практики не знаю, при наличии времени больше внимания уделил бы возможным исключениям.

### Модуль news_api
API для получения новостей из БД. Лучших практик по Flask так же не знаю. При наличии времени уделил бы больше внимания логированию (видел, как прикрутить тот же loguru). Получение данных через ORM. По необходимости на реальном проекте также можно (нужно) организовать запуск как wsgi через gunicorn.

### БД
Используется контейнер postgres:11, данные БД вынесены через volume, инициализация проходит скриптом init.sql.

### Запуск
Запуск через оркестратор docker-compose.
```
docker-compose up -d --build
```
