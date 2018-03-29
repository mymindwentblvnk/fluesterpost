import requests

from flask_restful import Resource, reqparse

from twython import Twython
from twilio.rest import import Client

import settings


class DefaultResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        parser.add_argument('token')
        args = parser.parse_args()

        if settings.TOKEN:
            assert args['token'] == settings.TOKEN

        try:
            self.fluester(args['text'])
            return 200
        except Exception:
            return 500


class Twitter(DefaultResource):

    def fluester(self, text):
        twitter = Twython(settings.TWITTER_APP_KEY,
                          settings.TWITTER_APP_SECRET,
                          settings.TWITTER_OAUTH_TOKEN,
                          settings.TWITTER_OAUTH_TOKEN_SECRET)
        twitter.update_status(status=text[:settings.TWITTER_STATUS_LENGTH])


class Slack(DefaultResource):

    def fluester(self, text):
        requests.post(settings.SLACK_WEBHOOK_URL, json={'text': text})


class Twilio(DefaultResource):

    def fluester(self, text):
        client = Client(settings.TWILIO_ACCOUNT_SID,
                        settings.TWILIO_AUTH_TOKEN)
        client.api.messages.create(to=settings.TWILIO_TO_NUMBER,
                                   from_=settings.TWILIO_FROM_NUMBER,
                                   body=text)
