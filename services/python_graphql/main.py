from flask import Flask
from flask_graphql import GraphQLView
from graphql_demo.schema.schema import schema
from database.init_db import init_db

app = Flask(__name__)


def run_server():
    app.debug = True
    app.add_url_rule(
        '/graphql_demo',
        view_func=GraphQLView.as_view(
            'graphql_demo',
            schema=schema,
            graphiql=True
        )
    )
    app.run()


if __name__ == '__main__':
    init_db()
    run_server()
