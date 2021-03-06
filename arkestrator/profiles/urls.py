from django.conf.urls.defaults import *
from django.contrib.auth.views import password_change, password_reset
import views

urlpatterns = patterns('',
        url(r"^(?P<user_id>\d+)/$", views.view_profile, name='view-profile'),
        url(r"^edit/$", views.edit_info, name='edit-info'),
        url(r"^preferences/$", views.edit_prefs, name='edit-prefs'),
        url(r"^$", views.list_users, name='list-users'),
)
