typescript: _setup
    # npm i @hey-api
    # npm i -D openapi-typescript typescript
    # npx openapi-typescript openapi.yml -o ts/v1.d.ts

    # npm install @hey-api/client-fetch && npm install @hey-api/openapi-ts -D
    # npx @hey-api/openapi-ts -i openapi.yml -o ts -c @hey-api/client-fetch

    # npm i -D openapi-typescript typescript
    # npx openapi-typescript openapi.yml -o ts/v1.d.ts

    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g typescript-fetch -o ./ts

fastapi: _setup
    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g python-fastapi -o ./fastapi

flask_install:
    just flask ../api

flask target: _setup
    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g python-flask -o {{target}} \
        --additional-properties=serverPort=1122

_setup:
    npm install @openapitools/openapi-generator-cli
