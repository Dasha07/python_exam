from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'home$', home, name='home'),
    url(r'register$', register, name='register'),
    url(r'login$', login, name='login'),
    url(r'logout$', logout, name='logout'),
    url(r'^add/(?P<quote_id>\d+)$', add, name='add'),
    url(r'^create/$', create, name='create'),
    url(r'^drop/(?P<quote_id>\d+)$', drop, name='drop'),
    url(r'^show_user/(?P<user_id>[0-9]+)$', show_user, name='show_user')
]
