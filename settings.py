import os


TOKEN = os.environ.get('TOKEN') if os.environ.get('TOKEN') else ''  # If set, post request has to send exactly this token


# Twitter API Information
TWITTER_APP_KEY =  os.environ.get('TWITTER_APP_KEY') if os.environ.get('TWITTER_APP_KEY') else ''
TWITTER_APP_SECRET = os.environ.get('TWITTER_APP_SECRET') if os.environ.get('TWITTER_APP_SECRET') else ''
TWITTER_OAUTH_TWITTER_OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN') if os.environ.get('TWITTER_OAUTH_TOKEN') else ''
TWITTER_OAUTH_TWITTER_OAUTH_TOKEN_SECRET_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET') if os.environ.get('TWITTER_OAUTH_TOKEN_SECRET') else ''
TWITTER_STATUS_LENGTH = 280


# Slack Webhooks
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL') if os.environ.get('SLACK_WEBHOOK_URL') else ''
