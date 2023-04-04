## Разворачиваем проект


1. Клонируем проект
```shell
$ git clone git@github.com:IUseAll16Letters/drf_testovoe_230404.git && cd drf_testovoe_230404 && git checkout 1.start_project
```

2. Стартуем докер, собираем контейнеры
```shell
$ docker-compose build
```

3. Накатываем миграции, создаем админыча
```shell
$ docker-compose run --service-ports django python manage.py migrate && docker-compose run --service-ports django python manage.py createsuperuser
```

Стартуем сабж
```shell
$ docker-compose run --service-ports django python manage.py runserver 0.0.0.0:8000
```

### Основные урлы
1. http://127.0.0.1:8000/swagger/ - swagger
2. http://127.0.0.1:8000/api/v1/ - корень api