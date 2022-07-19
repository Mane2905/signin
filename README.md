# Signin

This is the backend for Signin.
The production stack used is as follows:

* Ubunut Server LTS 18.04
* Nginx as the web-facing server and reverse proxy
* Gunicorn which runs the Django web application
* PostgreSQL as the relational database

For development purposes, we use Django's default stack (development server, provided by the `staticfiles` app and SQLite)