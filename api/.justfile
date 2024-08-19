network := 'task'

run:
    # create network for api and db to live in
    if docker network ls --filter name=^{{network}}$ --format "\{\{.Name\}\}" | grep -w "{{network}}"; then \
        docker network create {{network}}; \
    fi
    just postgres
    just api

api:
    docker rm -f task-api
    docker build -t task-api .
    docker run --network {{network}} -p 1122:1122 -p 42069:1122 --name task-api task-api

psql:
    psql -h localhost -p 1121 -U postgres

postgres:
    just stop_postgres
    docker run -p 1121:5432 --name task-postgres \
        --network {{network}} \
        -v /dbdata/task:/var/lib/postgresql/data \
        -e POSTGRES_PASSWORD=postgres -d \
        postgres

stop_postgres:
    just stop_container task-postgres

docker_network:
    docker network create task

stop_container name:
        docker rm -f {{name}}