# mosmetro_test
Сервис по парсингу новостей с сайта московского метро в БД + API, по которому эти новости можно получить

### Модуль news_parser
Парсит сайт метро и записывает их в БД через ORM. Работает в бесконечном цикле. C beautifulsoup не работал, лучшие практики не знаю, при наличии времени больше внимания уделил бы возможным исключениям.

### Модуль news_api
API для получения новостей из БД. Лучших практик по Flask так же не знаю. При наличии времени уделил бы больше внимания логированию (видел, как прикрутить тот же loguru). Получение данных через ORM.

### БД
Предполагается использование postgresql 11. Структура таблицы:
```
 create table metro_news
 (
     news_id   integer not null
         constraint metro_news_pkey
             primary key,
     header    text,
     url_pic   varchar,
     url_news  varchar,
     date      date,
     parsed_at timestamp
 );

 alter table metro_news
     owner to postgres;
```

### Запуск
Каждый из модулей предполагается к запуску в докере в отдельном контейнере. На реальном проекте для модулей нужно было бы сделать разные requirements.txt, но для ускорения здесь один. БД предполагается отдельностоящая, но можно запустить все вместе в контейнерах (сделать новый образ из postgres:11 с init скриптом на базе описания выше) с docker-compose, 
данные БД указываются в файле конфигурации. На реальном проекте вынес бы в переменную окружения.

```
docker build -t news_api -f Dockerfile_news_api .
docker build -t news_parser -f Dockerfile_news_parser .

docker run --rm --name news_parser news_parser
docker run --rm --name news_api -p 5000:5000 news_api

```
