# ebay-oauth-python-client
To use automation with ebay APIs you need to give a consent an app will be using your business account. During this consent you get refresh tokens which last for
some time (hours or days). Then again you'll need to give a consent. This part is not automatable and user has to pass captcha from ebay.
This app asks you login and password and then show up consent page (via selenium in ebay modules). After that it stores received refresh tokens to file.
