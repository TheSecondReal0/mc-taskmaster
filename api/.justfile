run:
    docker rm -f task-api
    docker build --no-cache -t task-api .
    docker run -d -p 1122:1122 --name task-api task-api

psql:
    psql -h localhost -p 1121 -U postgres

postgres:
    just stop_postgres
    docker run -p 1121:5432 --name task-postgres \
        -v /dbdata/task:/var/lib/postgresql/data \
        -e POSTGRES_PASSWORD=postgres -d \
        postgres

stop_postgres:
    just stop_container task-postgres

stop_container name:
        docker rm -f {{name}}