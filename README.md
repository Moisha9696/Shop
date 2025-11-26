# Устновка Django

```commandline
pip install django
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

### тестирование почты

```commandline
python manage.py shell
```

```commandline
from django.core.mail import EmailMessage   
email = EmailMessage(subject='Subject',body='This is the body of the email.',to=['ayukhovich@gmail.com']) 
email.send()
```
