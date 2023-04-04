# Background

- This repo for background job consume rabbitMQ to run ansible


- Related repo: 
    - [fastapi-template](https://github.com/phucln-kiotviet/fastapi-template)



- Create database:

```
create database background;
```

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

## Create database mariadb

- From docker:


```
docker run -d --name mariadb_background --env MARIADB_USER=mariadb --env MARIADB_PASSWORD=mariadb --env MARIADB_ROOT_PASSWORD=mariadb_root mariadb:10.7
```

- Check ip of container:

```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb_background
```

- Create database:

```
create database background;
```