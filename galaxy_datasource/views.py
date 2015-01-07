from django.views import generic
import urlparse
import urllib
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from galaxy_datasource.utils import export_redirect

def index(request):
    return render(request, 'galaxy_datasource/index.html', {
        'session_key': request.session._get_or_create_session_key(),
        'r': export_redirect(request, 'http://localhost:8000/galaxy_datasource/data/?search="blah"&filetype=tabular&retmode=1'),
        'request': request,
        })

def data(request):
    return render(request, 'galaxy_datasource/echo.txt',{
        'data': request.__str__()
        })

