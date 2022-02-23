@echo off

echo Making migrations
python manage.py makemigrations
echo Migrating
python manage.py migrate