from django.conf.urls import url

from . import views
from .views import EntityListView
from django.views.generic import RedirectView

app_name='cdradmin'
urlpatterns = [
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^entitytype/$', views.EntityListView.as_view(), name='entity_partnertype'),
    # url(r'^entity_partner/$', views.entity_partner, name='entity_partner'),
]
