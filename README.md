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
6. In case superuser must be created run: python manage.py createsuperuser 
7. Now your project is ready to run, run: python manage.py runserver 