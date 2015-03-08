from django.conf.urls import patterns, include, url

from django.contrib import admin
from users import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'healthnet.views.home', name='home'),
     #url(r'^', include(users.views.logon)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^calendar/$', views.calendar, name='calendar'),
)


admin.autodiscover()
