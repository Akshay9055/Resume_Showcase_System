from os import stat
from . import views
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.loginAccount, name='login'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('profile', views.profile, name='profile'),

    path('view_resume', views.view_resume, name='view_resume'),
    path('help', views.help, name='help'),
    path('settings', views.settings, name='settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)