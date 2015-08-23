from django.conf.urls.defaults import *
from piston.resource import Resource
from testproject.api.handlers import UserHandler, UserCreateHandler


UserResourceHandler = Resource(UserHandler)
UserResourceCreateHandler = Resource(UserCreateHandler)

urlpatterns = patterns('',
   url(r'^user/$', UserResourceCreateHandler),
   url(r'^user/(?P<user_id>\d+)/$', UserResourceHandler),
)