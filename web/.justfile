build_web: 
    docker build --network=host -t task-frontend .

web:
    just stop_web
    just build_web
    docker run -d --network=host --name task-frontend -p 4173:3000 task-frontend

stop_web:
    just stop_container task-frontend

stop_container name:
        docker rm -f {{name}}

