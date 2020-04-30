Template repository to deploy cannabis strain recommendation web API 



## set environment variable for running locally and remotely on heroku config:set

```bash
FLASK_APP="______"
DATABASE_URL="sqlite:///some-db.db"
SECRET_KEY="SECRET_KEY"
API_KEY="password"

```

## Running Locally

```bash
FLASK_APP=web_app flask run
​
​
FLASK_APP=web_app flask db init
LASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade

```

## refreshing db after db init, migrate, and upgrade steps
run locally and paste url in browser: '/db-refresh?api_key=API_KEY'




## Deploying to heroku

```bash
heroku create # optionally provide a name... "heroku create my-app-name"
git push heroku master # deploys repo to heroku

```

## migrate database to PostgreSQL on Heroku

```bash
heroku run bash

FLASK_APP=web_app flask db init
LASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade

```

## Configure heroku with environment variable keys

```bash

heroku config:set API_KEY="____"
heroku config:set FLASK_APP="______"
heroku config:set SECRET_KEY="SECRET_KEY"
heroku config:set API_KEY="password"

```
## refreshing db after db init, migrate, and upgrade steps
run remotely on heroku and paste url in browser: '/db-refresh?api_key=API_KEY'

## troubleshooting in heroku

```bash
heroku logs --tail

```

## different routes for running app

```bash
'/': welcome screen
'/strains.json': strain db api
'/recommendation_form': user import form to get strain recommendation
'/ml_strains.json': AI created strain descriptions api

```