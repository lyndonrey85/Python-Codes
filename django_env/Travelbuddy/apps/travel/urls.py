from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addplan$', views.addplan, name="addplan"),
    url(r'^travel$', views.travel, name="travel"),
    url(r'^join$', views.join, name="join"),
    url(r'^create$', views.create, name="create"),
    url(r'^delete$', views.delete, name="delete"),
    url(r'^(?P<travel_id>\d+)$', views.show)
    # url(r'^(?P<travel_id>\d+)/create$', views.create_additional, name="create_add")
]