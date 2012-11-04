<<<<<<< HEAD
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'breakin.views.home', name='home'),
    # url(r'^breakin/', include('breakin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
=======
import os
import os.path
from django.views.generic.simple import direct_to_template
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *
from bookmarks.views import *
#from feeds.views import *
import settings 

from django.shortcuts import get_object_or_404, render

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# Browsing
	(r'^$', news_feed),
	(r'^board/$', bulletin_board),
	
	# Admin stuff
	(r'^admin/', include(admin.site.urls)),
		
	# Account Management -- needs to be integrated
	(r'^save/$', bookmark_save_page),
	(r'^newssave/$', newsbookmark_save_page),
		
)

if settings.DEBUG:
  urlpatterns += staticfiles_urlpatterns()
>>>>>>> b325b8f... StoryShare
