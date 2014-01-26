from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url('^$', 'index', name="index"),
)
