from django.conf.urls.defaults import *
from django.http import HttpResponse

def testify(request):
    return HttpResponse('testify!')

urlpatterns = patterns('',
    url(r'^included/', include('decorator_include.tests.included2')),
    url(r'^test/$', testify, name='testify'),
)
