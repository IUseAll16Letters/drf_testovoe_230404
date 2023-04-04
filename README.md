## Разворачиваем проект


1. Клонируем проект
```shell
$ git clone git@github.com:IUseAll16Letters/drf_testovoe_230404.git && cd drf_testovoe_230404 
```

2. Стартуем докер, собираем контейнеры
```shell
$ docker-compose build
```

3. Накатываем миграции
```shell
$ docker-compose run --service-ports django python manage.py migrate
```

Создаем админыча
```shell
$ docker-compose run --service-ports django python manage.py createsuperuser
```
Стартуем сабж
```shell
$ docker-compose run --service-ports django python manage.py runserver 0.0.0.0:8000
```
