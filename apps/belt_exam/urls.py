from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'home$', home, name='home'),
    url(r'register$', register, name='register'),
    url(r'login$', login, name='login'),
    url(r'logout$', logout, name='logout'),
    url(r'^add/(?P<user_id>\d+)$', add, name='add')
]
