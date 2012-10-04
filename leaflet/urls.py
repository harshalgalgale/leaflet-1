from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Main
urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^create/(?P<user_id>\d+)/new/$','create', name='create'),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

# Auth and Accounts
urlpatterns += patterns('accounts.views',
	url(r'^register/$', 'registration_request', name='registration'),
	url(r'^login/$', 'login_request', name='login'),
	url(r'^logout/$', 'logout_request', name='logout'),
	url(r'^profile/(?P<user_id>\d+)/$', 'profile', name='profile')
)
