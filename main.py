"""Gets refresh token for eBay account by opening consent page (via selenium in ebay modules). Refresh tokens are needed
to generate access tokens to work with ebay APIs"""

import os, sys
from write_refr_token_to_file import write_refr_token_to_file
# for pyInstaller
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
from oauthclient.credentialutil import credentialutil
import test.TestUtil as TestUtil
from oauthclient.model.model import environment
from oauthclient.oauth2api import oauth2api
import logging
from cmd_args_settings import args, application_path, redirect_url, app_scopes
import time


if __name__ == "__main__":
    # Set root logger with Debug level. Not best idea because all imported modules using root logger will also output their
    # internal logs
    # logging.getLogger().setLevel(logging.DEBUG)
    app_config_path = args.config
    # For checking how pyInstaller manages with __file__
    # logging.debug(f'1: {os.path.split(__file__)[0]}')
    # logging.debug(f'2: app_config_path {app_config_path}')
    credentialutil.load(app_config_path)
    oauth2api_inst = oauth2api()
    signin_url = oauth2api_inst.generate_user_authorization_url(environment.PRODUCTION, app_scopes)
    code = TestUtil.get_authorization_code(signin_url, application_path, redirect_url, args.email, args.password,
                                           args.proxy)
    user_token = oauth2api_inst.exchange_code_for_access_token(environment.PRODUCTION, code)
    # this goes to Zapier to refresh token
    # user_token = oauth2api_inst.get_access_token(environment.PRODUCTION, user_token.refresh_token, app_scopes)
    # print('\n *** test_refresh_user_access_token ***:\n', user_token)
    email = args.email
    if args.email is None:
        email = input("input email for which you've just consented\n")
    data_to_save = {email: user_token.refresh_token}
    write_refr_token_to_file(data_to_save, args.output_to)
    print(f"refresh token was successfully written to {args.output_to}")
    time.sleep(10)
