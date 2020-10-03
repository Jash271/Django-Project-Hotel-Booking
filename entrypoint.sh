#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

wget http://127.0.0.1:8000/Operations/ManagerPopulate
