# backend_django

#### Запуск для тестирования API:
Скопировать проект
```
git clone git@github.com:hackathone-prosept-team2/backend_django.git
```

Если ранее уже скопировали и были обновления на бэке, надо подтянуть их из гита (ветка main):
```
git pull
```

Создать файл .env (можно переименовать .env.example в .env)

Перейти в папку deploy внутри проекта
```
cd backend_django/deploy/
```

Запустить сборку контейнеров
```
docker-compose up -d --build
```

После запуска контейнеров: добавить миграции в базу, собрать статику для документации
```
docker exec -it prosept_back python manage.py migrate
docker exec -it prosept_back python manage.py collectstatic --noinput
```

Создать суперпользователя для админки:
```
docker exec -it prosept_back python manage.py migrate
```

Доступные ссылки:
http://127.0.0.1/api/schema/swagger/#/ - документация API
http://127.0.0.1/admin - админ-панель