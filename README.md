# YANDEX & PROSEPT HACKATHON: Сервис сопоставления товаров Просепт и наименований дилеров. Way2IT (Команда 2).
http://81.31.246.5/ <br>
данные для пробного входа на сайт и в админ-панель
```
email: admin@admin.admin
password: Password-123
```
## Архивы и фото
Вставить сюда фотки с сайта

##  FRONTEND: 
https://github.com/hackathone-prosept-team2/frontend

##  DATA-SCIENCE: 
https://github.com/hackathone-prosept-team2/data-science

##  BACKEND: 
### Инструменты:
![image](https://img.shields.io/badge/Python%203.11-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django%204.2-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest%203.14-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![image](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![image](https://img.shields.io/badge/Pytest-86D46B?style=for-the-badge&logo=redux%20saga&logoColor=999999)

### Доступ в админ-панель:
http://81.31.246.5/admin 
```
email: admin@admin.admin
password: Password-123
```

### API-документация:
http://81.31.246.5/api/schema/swagger/#
```
Авторизация через headers:
Authorization: Token <access-token>
```

### Тестирование бэкенда:
![image](https://github.com/hackathone-prosept-team2/backend_django/blob/main/presentation/coverage.png)

### Описание возможностей
| Метод  | Endpoint                                     | Назначение                                                               |
|:-------|----------------------------------------------|--------------------------------------------------------------------------|
| POST   |/api/v1/auth/token/login/                     | Получение токена для пользователя (вход) |
| POST   |/api/v1/auth/token/login/                     | Уничтожение токена для пользователя (выход)  |
| GET    |/api/v1/users/                                | Получение списка пользователей  |
| POST   |/api/v1/users/                                | Создание нового пользователя |
| GET    |/api/v1/users/{id}/                           | Просмотр информации о пользователе с id {id} |
| GET    |/api/v1/users/me/                             | Просмотр информации о текущем пользователе  |
| GET    |/api/v1/attributes/                           | Полный список словарей моделей-атрибутов  |
| GET    |/api/v1/dealers/                              | Получение списка дилеров |
| GET    |/api/v1/dealers/{id}/                         | Просмотр информации о дилере с id {id} |
| GET    |/api/v1/dealers/report/                       | Отчет по дилерам и их ключам |
| GET    |/api/v1/keys/                                 | Список ключей дилеров с возможностью фильтрации по параметрам |
| GET    |/api/v1/keys/{id}/                            | Информация о ключе дилера с id {id} |
| GET    |/api/v1/keys/{id}/matches/                    | Список подобранных возможных продуктов к этому ключу |
| POST   |/api/v1/keys/{id}/choose_match/               | Выбор 1 продукта для сопоставления с ключем дилера |
| POST   |/api/v1/keys/{id}/decline_matches/            | Пометка всех предложенных продуктов как неподходящие |
| GET    |/api/v1/keys/{id}/prices/                     | Список цен к ключу дилера |
| GET    |/api/v1/keys/export/                          | Выгрузка сопоставленных ключей и продуктов с фильтром по новым/дате/периоду |
| POST   |/api/v1/prices/                               | Загрузка в базу данных цен из предоставленного Просепт файла и запуск системы подбора |
| DELETE |/api/v1/prices/                               | Удаление из базы данных всех цен, связанных рекомендаций и установленных связей |
| GET    |/api/v1/products/                             | Список продуктов компании |
| GET    |/api/v1/products/{id}/                        | Просмотр информации о продукте компании с id {id} |


## Запуск проекта
### Переменные окружения
Файл .env хранится в корневой папке проекта; пример заполнения в .env.example.

### Запуск с установленным Docker
Копировать проект в папку целиком (для запуска контейнеров достаточно .env в корне проекта и папки /infra)
```
git clone git@github.com:hackathone-prosept-team2/backend_django.git
```
Перейти в папку deploy и запустить сборку контейнеров
```
cd backend_django/deploy
docker compose up -d
```
Добавить миграции и собрать статику
```
docker exec -it career_back python manage.py migrate
docker exec -it career_back python manage.py collectstatic --noinput
```
Сайт доступен по адресу http://127.0.0.1/

### Наполнение проекта фикстурами
Фикстуры всех атрибутов + 50 студентов + 1 админ (admin@admin.admin / password-123) для проверки работы сайта
```
docker exec -it career_back python manage.py loaddata static/fixtures/data.json
```

Добавить только модели атрибутов (статичные модели для фильтров и атрибутов соискателей)
```
docker exec -it career_back python manage.py add_attributes
```

## Команда
### Project Manger
Марина Нюнякина
### Backend:
[Руслан Атаров](https://github.com/ratarov) <br>
[Филипп Пыхонин](https://github.com/caveinfix)<br>
### Design:
[Решетняк Анастасия](https://www.behance.net/015d9f71)<br>
[Евгения Постникова](https://www.behance.net/eugi_eugenia)<br>
Вера Карулина
### Frontend:
[Влад Мещеринов](https://github.com/beardy-raccoon) <br>
[Артем Никифоров](https://github.com/Art-Frich) <br>
[Любимов Ярослав](https://github.com/Yanseses)
