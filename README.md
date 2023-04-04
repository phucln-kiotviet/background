# Background template

- This repo for background job consume rabbitMQ to run ansible


- Related repo: 
    - [fastapi-template](https://github.com/phucln-kiotviet/fastapi-template)



- Create database:

```
create database background;
```

## Todo

- Move `config.py` to `env.py` so we can reload app with new config. Does not need rebuild.

## Alembic

- Initial migration with command:

```
alembic init migrations
```

- Create first revision:

```
alembic revision --autogenerate -m "create tables Ansible"
```

- Run command to create table.

```
alembic upgrade head
```

## Local test

- Consumer:

```
python3 main.py
```

- Producer test:

```
python3 producer_test.py
```