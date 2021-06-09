Добро пожаловать в ItHouse xD

Для запуска с помощью docker-compose собрать проект с помощью makefile:
make build

Для запуска вручную:
sudo docker-compose build
sudo docker-compose up

Если не работает, то,
чтобы удалить всё из БД и применить миграции заново:
sudo docker-compose build
sudo docker-compose up
sudo docker-compose exec db psql -U slayer -d itdb

SELECT 'drop table if exists "' || tablename || '" cascade;' as pg_tbl_drop
FROM pg_tables
WHERE schemaname='public';

копируем и вставляем код, который нам выдало в ответ после
последней команды и выполняем дроп таблиц,
далее:

sudo docker-compose exec web python3 manage.py makemigrations

sudo docker-compose exec web python3 manage.py migrate

sudo docker-compose exec web python3 manage.py createsuperuser
