# Diplom_django
Инструкции по установке и первому запуску.

Для запуска проекта необходимо:

Установить необходимые модули:
pip install -r requirements.txt

Провести миграцию:
.manage.py migrate

Загрузить базу данных:
.manage.py loaddata db.json

Выполнить команду для запуска проекта:
python manage.py runserver
