from .settings import *
import os

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# DBHOST is only the server name, not the full URL
hostname = os.environ['DBHOST'] if 'DBHOST' in os.environ else ''
dbname = os.environ['DBNAME'] if 'DBNAME' in os.environ else ''
dbuser = os.environ['DBUSER'] if 'DBUSER' in os.environ else ''
dbpassword = os.environ['DBPASS'] if 'DBPASS' in os.environ else ''

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dbname,
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': dbuser + "@" + hostname,
        'PASSWORD': dbpassword
    }
}
