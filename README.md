Template repository to deploy cannabis strain recommendation web API 

## Recipe

```bash

git init
touch README.md
pipenv --python 3.7
pipenv install Flask Flask-SQLAlchemy Flask-Migrate python-dotenv requests bs4 gunicorn psycopg2-binary
touch .gitignore
touch .env
mkdir web_app && cd web_app
touch __init__.py
touch Procfile
mkdir routes
mkdir services
touch models.py
touch routes/home_routes.py
touch routes/recommendation_routes.py

```

## Running Locally

```bash
export FLASK_APP="web_app" #only once
flask run

```

## To Do List

* Integrating machine learning prediction as service
* Connecting application with database
* Deploying application on Heroku
* Integrating with Heroku PostgreSQL database
* Tests/CI
* Reproducible build scripts
* Containerize the web application