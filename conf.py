import os

# Debug mode gives nicer error messages and enables serving of static media
# directly from the Python process.  It is highly insecure, however, so be sure
# to turn it off before going to production.
DEBUG = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nx!9ne@6oj0(=3hzhno6!ed$4+mxu1n4gy727fjb3n^$e7sc0s'

# This tells all of the Clutch systems how to talk to your PostgreSQL database,
# so if you are running it on a different host, you should change the host and
# port information here (as well as any security credentials your setup
# requires.)
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()
# DATABASES['default'].update({
#     'NAME': 'clutch',
#     'USER': 'clutch',
#     'PASSWORD': '',
#     'HOST': '127.0.0.1',
#     'PORT': '5432',
# })

# Enter your Amazon Web Services S3 access key, secret, and the bucket name.
# (This is necessary for hybrid native/html application framework ONLY.)
AWS_ACCESS_KEY = ''
AWS_ACCESS_SECRET = ''
AWS_BUCKET_NAME = ''

# The host and port that the Clutch RPC server should run on.
CLUTCH_RPC_HOST = '0.0.0.0'
CLUTCH_RPC_PORT = os.environ['PORT']

# This is the URL that the tunnel should use to communicate with the Clutch
# RPC server. This may differ from the CLUTCH_RPC_HOST and the CLUTCH_RPC_PORT
# if the RPC server is running on a different servers.
CLUTCH_RPC_URL = 'http://ab-testing-rpc.herokuapp.com:80/'

# The host and port that the Clutch Tunnel server should run on.
CLUTCH_TUNNEL_HOST = '0.0.0.0'
CLUTCH_TUNNEL_PORT = os.environ['PORT']
