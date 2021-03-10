# Разработка CRUD приложения с использованием Python и Django

Token (JSON Web Token) аутентификация пользователей с реализацией endpoints:

* `POST /api-token-auth/` - получение токена при вводе username, password 
* `GET /api/v1/users/` - получение данных списка пользователей 
* `GET /api/v1/users/<id>/` - получение данных пользователя по id
* `POST /api/v1/users/` - создание пользователя
* `DELETE /api/v1/users/<id>/` - удаление пользователя по id
* `PUT /api/v1/users/<id>/` - изменение пользователя по id
* `PATCH /api/v1/users/<id>/` - частичное изменение пользователя по id
