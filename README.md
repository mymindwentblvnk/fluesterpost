# fluesterpost
A super slim Flask application to spread the word you give it.

## Endpoints

At the moment the following APIs are supported. To use it, enter the needed information in settings.py.

* Twitter API (https://apps.twitter.com/)
* Slack Webhooks (https://api.slack.com/incoming-webhooks)

## How

Send post requests to the Flask endpoint of your choice with the following information

```
{
 'text': 'The text to send',
 'token': '<the_token_if_set_in_settings.py>'
}
```

## Example

* Create a environment with `make env`
* Run server with `python app.py`
* `make curl text="This is my new Twitter status." token="<THE_TOKEN>" host=localhost:5000 endpoint=twitter`

![Profit](https://i.imgur.com/6M8PjSQ.png)

## TODO

* More endpoints to come
  * Discord
  * Telegram
  * E-Mail
  * Et Cetera
* Make use of environment variables
* Tests
