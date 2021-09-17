 create table if not exists metro_news
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