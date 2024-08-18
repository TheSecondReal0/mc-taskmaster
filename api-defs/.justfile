typescript:
    # npm i @hey-api
    # npm i -D openapi-typescript typescript
    # npx openapi-typescript openapi.yml -o ts/v1.d.ts

    # npm install @hey-api/client-fetch && npm install @hey-api/openapi-ts -D
    # npx @hey-api/openapi-ts -i openapi.yml -o ts -c @hey-api/client-fetch

    # npm i -D openapi-typescript typescript
    # npx openapi-typescript openapi.yml -o ts/v1.d.ts

    npm install @openapitools/openapi-generator-cli
    npx @openapitools/openapi-generator-cli generate -i openapi.yml -g typescript-fetch -o ./ts


