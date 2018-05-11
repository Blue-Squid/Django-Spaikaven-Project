from django.conf.urls import url,include
from project.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^validate_user$',validate_user, name = 'validate_user'),
    url(r'^home$', home, name='home'),
    url(r'^profile$', profile, name='profile'),
    url(r'^view_msg$', view_msg, name='view_msg'),
    url(r'^log_out$', log_out, name='log_out'),
    
]
