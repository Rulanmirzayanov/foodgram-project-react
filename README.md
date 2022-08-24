# Дипломный проект — сайт Foodgram, «Продуктовый помощник».
![example workflow](https://github.com/Rulanmirzayanov/foodgram-project-react/actions/workflows/maim.yml/badge.svg)
## Описание

Онлайн-сервис и API для него. На этом сервисе пользователи 
могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

## Установка

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
