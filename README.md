# Signin

This is the backend for Signin.
The production stack uses PostgreSQL as the relational database

For development purposes, we use Django's default stack (development server, provided by the `static` app and SQLite)

To run the project: 
1. Install all dependancies as given in requirements.txt : pip install requirements.txt
2. Since the project uses postgresql in setttings.py change the fields of DATABASES appropriately.
3. Run: pip install makemigrations
4. Run: pip install migrate
5. Run: python manage.py collectstatic
6. To create superuser run: python manage.py createsuperuser
Additional steps to run google authentication
7. log on to admin panel and to add site put Domain name and Dispay name as 127.0.0.1:8000
8. in social application put client id and scret key
9. Select your Site in 'Available sites' and click the arrow to move it into 'Chosen sites'
10. Note you might have to change SITE_ID in settings.py to be the correct ID (probably 1 or 2 or 3).
11. Now your project is ready to run, run: python manage.py runserver 