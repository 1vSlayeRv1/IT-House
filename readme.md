<h1>Добро пожаловать в ItHouse xD</h1>
Для начала напишите свою google почту и пароль в файл env.dev <br>
<code>EMAIL_HOST_USER='ваш_google'</code> <br>
<code>EMAIL_HOST_PASSWORD='ваш_пароль'</code> <br>
Для запуска с помощью docker-compose собрать проект с помощью makefile: <br>
<code>make docker</code> <br>
Для запуска тестов, запустите docker и выполните: <br>
<code>make testd</code> <br>
Для запуска докера с применением миграций: <br>
<code>make dockerm</code> <br> <br>

Для запуска без докера: <br>
<code>make build</code> <br>
либо: <br>
<code>make run</code> (если вы уже до этого выполняли <code>make build</code> ) <br>
Затем: <br>
<code>make redis</code> <br>
<code>make celery</code> <br>

Для запуска докера вручную: <br>
<code>sudo docker-compose build </code> <br>
<code>sudo docker-compose up</code> <br>

Чтобы выполнить миграции в докере: <br>
<code>sudo docker-compose exec web python3 manage.py migrate</code> <br>

Если не работает, то, возможно проблемы с миграциями
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
