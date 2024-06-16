# Прототип сервиса мониторинга и адаптивного распределения заявок на обслуживание от маломобильных пассажиров

![enter image description here](https://github.com/imozi/accessible_transport/assets/29326762/85e6fcb9-6f9d-4358-8b38-24938960b99b)


### Запуск проекта локально в Docker

Чтобы запустить проект необходимо что бы был установлен на компьютере [Docker](https://docs.docker.com/engine/install/)

1.  `git clone https://github.com/imozi/accessible_transport.git`
2.  Перейти в папку accessible_transport
3.  Переименовать в папке backend файл .env.example в .env 
4. Переименовать в папке frontend файл .env.example в .env
5. Запустить команду в корне проекта `docker compose up -d` 

### После запуска будут доступны

#### Frontend

> Nuxtjs - http://localhost:3000

#### Backend

> Django admin - http://locahost:8000/admin 

#### Документация API 

> Swagger - http://localhost:8000/swagger

> Redoc - http://localhost:8000/redoc

##### Запуск проектов по отдельности в разных режимах
[Backend](https://github.com/imozi/accessible_transport/tree/main/backend#accessible_transport)

[Frontend](https://github.com/imozi/accessible_transport/tree/main/frontend#nuxt-3-minimal-starter)