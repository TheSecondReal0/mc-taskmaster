run:
    docker rm -f task-api
    docker build --no-cache -t task-api .
    docker run -d -p 1122:1122 --name task-api task-api