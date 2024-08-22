#!/usr/bin/env python3

import connexion

from openapi_server import encoder

from flask_migrate import Migrate

from flask_cors import CORS

from . import db

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder

    # Configure the database URI
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@task-postgres:5432/task'
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

    db.app = app.app
    db.init_app(app.app)
    # migrate = Migrate(app, db)

    CORS(app.app)

    app.add_api('openapi.yaml',
                arguments={'title': 'MC Taskmaster'},
                pythonic_params=True)

    app.run(port=1122)

if __name__ == '__main__':
    main()
