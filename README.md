# movie_rating
## Installing the requirements
```shell
pip install -r requirements.txt
```

## Reseting migrations and clearing the database
```shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm -f db.sqlite3
```

## Making migrations and creating superuser
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Running the local server
```shell
python manage.py runserver
```

## Creating groups
After running the server, login as admin. Create four groups-
- is_actor
- is_director
- is_production_company
- public_user

Test the application live on http://45.76.151.11:8000/
