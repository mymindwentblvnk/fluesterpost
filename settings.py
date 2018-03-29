import os


TOKEN = os.environ.get('TOKEN') if os.environ.get('TOKEN') else ''  # If set, post request has to send exactly this token


# Twitter
TWITTER_APP_KEY =  os.environ.get('TWITTER_APP_KEY') if os.environ.get('TWITTER_APP_KEY') else ''
TWITTER_APP_SECRET = os.environ.get('TWITTER_APP_SECRET') if os.environ.get('TWITTER_APP_SECRET') else ''
TWITTER_OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN') if os.environ.get('TWITTER_OAUTH_TOKEN') else ''
TWITTER_OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET') if os.environ.get('TWITTER_OAUTH_TOKEN_SECRET') else ''
TWITTER_STATUS_LENGTH = 280


# Slack
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL') if os.environ.get('SLACK_WEBHOOK_URL') else ''


# Twilio
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID') if os.environ.get('TWILIO_ACCOUNT_SID') else ''
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN') if os.environ.get('TWILIO_AUTH_TOKEN') else ''
TWILIO_FROM_NUMBER = os.environ.get('TWILIO_FROM_NUMBER') if os.environ.get('TWILIO_FROM_NUMBER') else ''
TWILIO_TO_NUMBER = os.environ.get('TWILIO_TO_NUMBER') if os.environ.get('TWILIO_TO_NUMBER') else ''
