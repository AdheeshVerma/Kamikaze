## Keys and secrets
Set up needed OAuth keys (in settings.py):

```
SOCIAL_AUTH_TWITTER_KEY = 'foobar'
SOCIAL_AUTH_TWITTER_SECRET = 'bazqux'
```
## Authentication backends

Define the oauth providers or method in `settings.py` in `SOCIAL_AUTH_AUTHENTICATION_BACKENDS`
For example.
```
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    ...
)
```

## Views

By default the google oauth view works on `/login/google-oauth2`. Remember to setup redirect URL on Google cloud console.
