from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.CatView.as_view(), name='cat'),
    url(r'^(?P<category2>[a-zA-Z0-9]+)/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<question_category>[a-zA-Z0-9]+)/(?P<pk>[a-zA-Z0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_category>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_category>[a-zA-Z0-9]+)/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]