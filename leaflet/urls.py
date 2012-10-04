from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',

	# Main
    url(r'^$', 'index', name='index'),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('accounts.views',
    
    #Auths
	url(r'^register/$', 'registration_request', name='registration'),
	url(r'^login/$', 'login_request', name='login'),
	url(r'^logout/$', 'logout_request', name='logout'),
)
