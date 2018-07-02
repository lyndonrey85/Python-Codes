from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<course_id>\d+)$', views.show, name='show'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^deletethis/(?P<id>\d+)$', views.delete, name='deletethis')
]