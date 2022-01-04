import os

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index(request: WSGIRequest):
    website_hostname = os.environ['WEBSITE_HOSTNAME'] if 'WEBSITE_HOSTNAME' in os.environ else 'Not available'
    dbhost = os.environ['DBHOST'] if 'DBHOST' in os.environ else 'Not available'
    context = {
        "website_hostname": website_hostname,
        "dbhost": dbhost,
    }
    return render(request, context=context, template_name='test_azure_django/home/index.html')
