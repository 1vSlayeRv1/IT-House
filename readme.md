<h1>Добро пожаловать в ItHouse xD</h1>

Для запуска с помощью docker-compose собрать проект с помощью makefile: <br>
<code>make build</code>

Для запуска вручную: <br>
<code>sudo docker-compose build </code> <br>
<code>sudo docker-compose up</code>

Если не работает, то,
чтобы удалить всё из БД и применить миграции заново: <br>
<code>sudo docker-compose build</code><br>
<code>sudo docker-compose up</code><br>
<code>sudo docker-compose exec db psql -U slayer -d itdb</code><br>

<code>SELECT 'drop table if exists "' || tablename || '" cascade;' as pg_tbl_drop
FROM pg_tables
WHERE schemaname='public';</code> <br>

копируем и вставляем код, который нам выдало в ответ после последней команды и <br>
выполняем дроп таблиц, далее:

<code>sudo docker-compose exec web python3 manage.py makemigrations</code><br>

<code>sudo docker-compose exec web python3 manage.py migrate</code><br>

<code>sudo docker-compose exec web python3 manage.py createsuperuser</code><br>
