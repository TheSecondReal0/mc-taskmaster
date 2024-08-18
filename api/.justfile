run:
    docker build -t task-api .
    docker run -d --name task-api task-api