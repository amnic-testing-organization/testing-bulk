from django.shortcuts import render
from django.http import HttpResponse
import django
import os
import platform
# Create your views here.

django_version= django.get_version()
runtime_version = platform.python_version()

config_key = "TEST_INT_VALUE"
secret_key = "SAMPLE_SECRET"

if secret_key in os.environ:
    secrets = os.environ['SAMPLE_SECRET']
else:
    secrets= "No secrets were found"

if config_key in os.environ:
    configs = os.environ['TEST_INT_VALUE']
else:
    configs= "No secrets were found"


def homePageView(request):
    return HttpResponse("""Hello From AMNIC !!<br/>
              Python_runtime_version : {0}<br/>  
              Django_framework_version :{1}<br/>
              secrets : {2}<br/>
              configs : {3}<br/>
                """.format(runtime_version,django_version,secrets,configs))
