# accessible_transport
Backend часть проекта

## Технологии

- [![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/) [![Django Rest Framework](https://img.shields.io/badge/-Django_Rest_Framework-092E20?style=flat)](https://www.django-rest-framework.org/)
- [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

## Описание
- --

## Установка (локальная)

- Убедиться, что у вас установлен python версии не ниже 3.11
- Установлен менеджер зависимостей poetry (подробнее об установке https://python-poetry.org/docs/#installation)
- Для начала работы с проектом клонируйте репозиторий и перейдите в папку с проектом ```cd accessible_transport/backend```
- Произведите установку зависимостей командами:
  - ```poetry shell```
  - ```poetry install```
- После установки зависимостей убедитесь в настроенном файле .env, правильных параметрах соединения к БД и создайте пустую БД
- Произведите миграции командами:
  - ```python manage.py makemigrations```
  - ```python manage.py migrate```
- После успешного применения миграций произведите загрузку предустановленных и тестовых данных в БД:
  - ```python manage.py loaddata tmp/allbase.json```
- После успешной загрузки данных запустите тестовый веб-сервер:
  - ```python manage.py runserver``` 


## Дополнительно
- Управление данными с помощью админки Django ```http://127.0.0.1/admin/```
  - логин - admin
  - пароль - 1
