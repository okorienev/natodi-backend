spin-up services app is dependant on:
```shell
docker-compose up -d
```

generate .env file from settings:
```shell
python -m cli dotenv generate
```

Run app
```shell
uvicorn app.main:app --reload
```

### Migrations
update database:
```shell
# non-docker
alembic upgrade head

# docker
docker-compose run server alembic upgrade head
```

downgrade database version by 1
```shell
# non-docker
alembic downgrade -1

# docker 
docker-compose run server alembic downgrade -1
```

generate new version (when editing models)
```shell
# non-docker
alembic revision --autogenerate -m <your_revision_slug>

# TODO add dockerized version
```