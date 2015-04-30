from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ngosearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^$", searchpage, name="index"),
    url(r"^index", searchpage, name="jobs"),
    url(r"^jobs", jobspage, name="jobs"),
    url(r"^employers", employerspage, name="employers"),
    url(r"^contactus", contactuspage, name="contactus"),
    url(r"^clients", clientspage, name="clients"),
    url(r"^aboutus", aboutuspage, name="aboutus"),
    url(r'^search/', include('haystack.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    
)
