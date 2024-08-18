typescript: _setup
    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g typescript-fetch -o ./../web/app/src/lib/api

fastapi: _setup
    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g python-fastapi -o ./fastapi

flask:
    just flask_to ../api

flask_to target: _setup
    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g python-flask -o {{target}} \
        --additional-properties=serverPort=1122

_setup:
    npm install @openapitools/openapi-generator-cli
