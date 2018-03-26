# fluesterpost
A Flask application to spread the word you give it.

## Endpoints

At the moment the following APIs are supported. To use it, enter the needed information in settings.py.

* Twitter API (https://apps.twitter.com/)
* Slack Webhooks (https://api.slack.com/incoming-webhooks)

## Example

* Create a environment with `make env`
* Run server with `python app.py`
* Curl e. g. the Twitter endpoint with `curl -d '{"text":"This is my new Twitter status.", "token": "<THE_TOKEN>"}' -H "Content-Type: application/json" -X POST http://localhost:5000/twitter`

![Profit](https://i.imgur.com/6M8PjSQ.png)

## TODO

* More endpoints to come
  * Telegram
  * Twilio
  * E-Mail
  * Et Cetera
* Make use of environment variables
* Tests
