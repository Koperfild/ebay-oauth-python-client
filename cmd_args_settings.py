"""In the beginning insertion for pyInstaller get working. Then filling argparser parameters for ebay seller account,
 ebay developer account, where to save received 'refresh token' some settings"""

import argparse
import os
import time
import sys

application_path = None
args = None

#Insertion for pyInstaller
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

default_output_path = 'refresh tokens.txt'
DEFAULT_DEVELOPER_CREDENTIALS = os.path.join(application_path, 'test', 'config', 'ebay-config-sample.json')
DEFAULT_PROXY = '5.79.73.131:13010'
redirect_url = "https://www.google.com/"
app_scopes = ['https://api.ebay.com/oauth/api_scope',
         'https://api.ebay.com/oauth/api_scope/sell.marketing.readonly',
         'https://api.ebay.com/oauth/api_scope/sell.marketing',
         'https://api.ebay.com/oauth/api_scope/sell.inventory.readonly',
         'https://api.ebay.com/oauth/api_scope/sell.inventory',
         'https://api.ebay.com/oauth/api_scope/sell.account.readonly',
         'https://api.ebay.com/oauth/api_scope/sell.account',
         'https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly',
         'https://api.ebay.com/oauth/api_scope/sell.fulfillment',
         'https://api.ebay.com/oauth/api_scope/sell.analytics.readonly',
         'https://api.ebay.com/oauth/api_scope/sell.finances',
         'https://api.ebay.com/oauth/api_scope/sell.payment.dispute',
         'https://api.ebay.com/oauth/api_scope/commerce.identity.readonly'
        ]

parser = argparse.ArgumentParser(description="Opens browser to ask consent from user to use his account by program"
                                             "which uses eBay APIs. eBay application credentials are in config file")
parser.add_argument("email",
                    help="email(login to eBay user account) to which ask consent",
                    nargs='?')
parser.add_argument("password",
                    help="password to eBay user account",
                    nargs='?')
parser.add_argument("-o",
                    "--output_to",
                    help="path relative or absolute where to save refresh token",
                    default=default_output_path)
parser.add_argument("-c",
                    "--config",
                    help="Specifies config file with developer app details",
                    default=DEFAULT_DEVELOPER_CREDENTIALS)
#if -p is provided but without value then const= will be set
#removed with always use proxy not to mess with settings
parser.add_argument("-p",
                    "--proxy",
                    # nargs='?',
                    # const=DEFAULT_PROXY)
                    default=DEFAULT_PROXY)
args = parser.parse_args()
#We require either both email and password or neither of the two
if len([x for x in [args.email,args.password] if x is not None]) == 1:
    print("Error in calling program. Either do not provide email and password or provide both")
    time.sleep(100)
    sys.exit(1)
