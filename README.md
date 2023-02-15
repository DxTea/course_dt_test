# Test task for Python Backend course 
###### from Doubletapp

---

## How to run

* Install `python 3.10` and `pipenv` (`pip install pipenv`) 
* Install requirements
* Create a file `.env` in `/src` like in **example below**
* Produce migrations
* Create SuperUser
* To start Telegram bot (`python manage.py run_bot`)
* To run server : `python manage.py runserver`
* To get admin panel: `http://localhost/admin`
* To get "me" info: `http://localhost/api/me/<tgid>`

## .env example:
`/src/.env` \
\
`TELEGRAM_TOKEN="sbfhdbhbdvhdbhjvb"`\
`SECRET_KEY="ddfnsjssjfnjsdnfjs"`\
`DB_ENGINE='django.db.backends.postgresql_psycopg2'`\
`DB_NAME='dt_testtask_db'`\
`DB_USER='user'`\
`DB_PASSWORD='1234'`\
`DB_HOST='localhost'`\
`DB_PORT='5432'`