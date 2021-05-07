import logging

logging.error('info log')
print('j')


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p")
# parser.add_argument("-p",
#                     "--proxy",
#                     nargs='?',
#                     const='20')
args = parser.parse_args()
print('jj')