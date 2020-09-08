Для начала загружаем модули
pip install -r requirements.txt

Создаем миграции приложения для базы данных
python manage.py migrate

Загружаем данные из подготовленной базы данных
manage.py loaddata db.json
