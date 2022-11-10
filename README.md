# k8s-workshop
Basics of Kubernetes - workshop

## Project initial setup

```shell
cd ~/dev
git clone https://github.com/Tomasz-Kluczkowski/k8s-workshop.git
cd k8s-workshop
pyenv virtualenv k8s-workshop
pyenv activate k8s-workshop
pip install -r requirements.txt
```

## Start local server in debug mode

```shell
flask --debug run
```

## Test the 1 and only route '/'
- go to your browser
- enter `http://127.0.0.1:5000`
- does it show `Hello, World!` ?

## Creating a docker image
- Create a file called `Dockerfile` in the root of the project 

```shell
touch Dockerfile
```

- Fill it in starting with image base

```shell
FROM python:3.10.2-slim
```

- build the image once you have completed the Dockerfile

```shell
docker build -t hello-world-app:1.0.0 .
```

- the image will be stored in your local docker registry which is good for now.

- we can push it to public docker repo in docker hub, all we need is for you to have an account
- register you account here if you don't have one: https://hub.docker.com/signup
- login to your docker account locally

```shell
docker login
```

- type username and password as requested in the terminal.
- to be able to push to docker hub we need to tag the existing image

```shell
docker tag hello-world-app:1.0.0 <your-docker-username>/hello-world-app:1.0.0
```

- push your image to docker hub

```shell
docker push <your-docker-username>/hello-world-app:1.0.0
```

## Database setup

We will use postgresql, sqlalchemy, psycopg2, flask-migrate to make database setup easy.

### Create our test database locally

I assume you have followed onboarding docs and you have local postgres user `postgres` with password `example`.
If that is not the case - use the one you created for your local postgres instance.

```shell
PGPASSWORD=example createdb -h localhost -p 5432 -U postgres k8s_workshop -w
```

## Install new requirements

```shell
pip install -r requirements.txt
```


## Initialise database (migrations) (only needed if there is no `migrations` folder)

```shell
flask db init
```

Output should look like this:

```shell
flask db init                                                                                                                                                                                                                                                                                                                                                                                                                                   ✔  k8s-workshop Py  9.2.20.1 Ruby  at 00:21:43 
  Creating directory /Users/tomaszkluczkowski/dev/k8s-workshop/migrations ...  done
  Creating directory /Users/tomaszkluczkowski/dev/k8s-workshop/migrations/versions ...  done
  Generating /Users/tomaszkluczkowski/dev/k8s-workshop/migrations/script.py.mako ...  done
  Generating /Users/tomaszkluczkowski/dev/k8s-workshop/migrations/env.py ...  done
  Generating /Users/tomaszkluczkowski/dev/k8s-workshop/migrations/README ...  done
  Generating /Users/tomaszkluczkowski/dev/k8s-workshop/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/tomaszkluczkowski/dev/k8s-workshop/migrations/alembic.ini' before proceeding.
```

## Generate initial migration (only needed if there is no `migrations` folder)

```shell
flask db migrate -m "initial migration"
```

Output should be like this:

```shell
flask db migrate -m "initial migration"                                                                                                                                                                                                                                                                                                                                                                                                       2 х  k8s-workshop Py  9.2.20.1 Ruby  at 00:28:40 
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
Generating /Users/tomaszkluczkowski/dev/k8s-workshop/migrations/versions/ec856abd4de5_initial_migration.py ...  done
```

## Apply migrations to the DB to create tables

```shell
flask db upgrade
```

Output will be like this:

```shell
flask db upgrade                                                                                                                                                                                                                                                                                                                                                                                                                                ✔  k8s-workshop Py  9.2.20.1 Ruby  at 00:28:59 
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> ec856abd4de5, initial migration
```

and you should see table `users` in your local postgres.
