network := 'task'

start:
    just run -d

run api_args="":
    # create network for api and db to live in
    if docker network ls --filter name=^{{network}}$ --format "\{\{.Name\}\}" | grep -w "{{network}}"; then \
        docker network create {{network}}; \
    fi
    just postgres
    just api {{api_args}}

api args="":
    docker rm -f task-api
    docker build --network=host -t task-api .
    docker run {{args}} --network {{network}} -p 1122:1122 --name task-api task-api

psql:
    psql -h localhost -p 1121 -U postgres task

postgres:
    just stop_postgres
    docker run -p 1121:5432 --name task-postgres \
        --network {{network}} \
        -v /dbdata/task:/var/lib/postgresql/data \
        -e POSTGRES_PASSWORD=postgres -d \
        postgres:16

stop_postgres:
    just stop_container task-postgres

docker_network:
    docker network create task

stop_container name:
    docker rm -f {{name}}
