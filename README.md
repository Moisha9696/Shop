# Устновка Django

```commandline
pip install djangorestframework
```

```commandline
python manage.py startapp your_app_name
```

# Запуск сервера
```commandline
python manage.py runserver
```

# Действия с БД


## Создание миграции 

```commandline
python manage.py makemigrations
```

## Применение миграции 

```commandline
python manage.py migrate
```
# Запуск сервера
```commandline
python manage.py runserver
```

## Создание сурер-пользователя
```commandline
python manage.py createsuperuser
```

Очень важно что после каждого изменения в моделях базы данных 
нужно сделать следующие шаги
1. [Создание миграции](Создание миграции)
2. [Применение миграции](Применение миграции)
