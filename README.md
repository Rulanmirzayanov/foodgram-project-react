![example workflow](https://github.com/Rulanmirzayanov/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# Дипломный проект — сайт Foodgram, «Продуктовый помощник».
## Описание

Онлайн-сервис и API для него. На этом сервисе пользователи 
могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

## Установка и запуск проекта локально

Клонировать репозиторий и перейти в него:

```
git clone https://github.com/Rulanmirzayanov/foodgram-project-react.git
cd backend
```

Создайте и активируйте виртуальное окружение для этого проекта:

```
python -m venv venv
```

```
source .\venv\Scripts\activate
```

Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции:

```
python manage.py migrate
```

Перейдите в директорию проекта:

```
cd backend
```

Создайте файл .env в директории backend и заполните его данными по этому 
образцу:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Запустите проект:
```
python manage.py runserver
```

## Установка и запуск проекта на сервере
### На странице [https://github.com/Rulanmirzayanov/foodgram-project-react.git]() сделать fork проекта в свой GitHUB
Зайдите в Settings → Secrets в вашем репозитории и добавьте следующие переменные:

```
HOST
# IP-адрес вашего сервера
USER
# имя пользователя для подключения к серверу
SSH_KEY
# ssh-ключ
PASSPHRASE
# фраза-пароль, если при создании ssh-ключа вы ее использовали 
DOCKER_USERNAME
# логин DockerHUB
DOCKER_PASSWORD
# пароль DockerHUB
DB_ENGINE, DB_NAME , POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT
# параметры из .env-файла
TELEGRAM_TO
# ID своего телеграм-аккаунта. Узнать свой ID можно у бота @userinfobot
TELEGRAM_TOKEN
# токен вашего бота, получить этот токен можно у бота @BotFather.
```

Установить docker, docker-compose на сервере в соответствии с официальной документацией;
- Зайти в дерикторию Infra и скопировать файлы docker-compose.yaml и nginx.conf на сервер

```
scp docker-compose.yml <username>@<server_ip>:/home/<username>/
scp nginx.conf <username>@<server_ip>:/home/<username>/
```
- Создать файл .env в дериктории infra:

```
touch .env
```
Шаблон наполнения .env-файла расположенного в папке infra
```
DB_ENGINE=django.db.backends.postgresql 
# указываем, что работаем с postgresql
DB_NAME=postgres 
# имя базы данных
POSTGRES_USER=postgres 
# логин для подключения к базе данных
POSTGRES_PASSWORD=postgres 
# пароль для подключения к БД (установите свой)
DB_HOST=db 
# название сервиса (контейнера)
DB_PORT=5432 
# порт для подключения к БД
```

- Зайти на сервер и выполнить миграции, импортировать данные, собрать статику и сделать суперпользователя

```
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate --noinput 
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
- Дополнительно наполнить DB тэгами и ингредиентами:

```
sudo docker-compose exec backend python manage.py load_tags
sudo docker-compose exec backend python manage.py load_ingredients
```
## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)