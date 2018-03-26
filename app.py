from flask import Flask
from flask_restful import Api

from api import Twitter, Slack


app = Flask(__name__)


api = Api(app)
api.add_resource(Twitter, '/twitter')
api.add_resource(Slack, '/slack')


if __name__ == '__main__':
    app.run()
