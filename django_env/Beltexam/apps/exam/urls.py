from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create$', views.create, name='create'),
    url(r'^(?P<friend_id>\d+)$', views.show, name='show'),
    url(r'^(?P<friend_id>\d+)$', views.add, name='add')
]