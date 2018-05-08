from django.conf.urls import url
from .views import index, addpost, searchtime, detailpost

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^addpost/$', addpost, name='addpost'),
	url(r'^searchtime/$', searchtime, name='searchtime'),
	url(r'^(?P<slug>[\w-]+)/$', detailpost, name='detailpost'),
]