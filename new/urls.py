from django.conf.urls import include, url
from . import views
urlpatterns=[
    url(r'^$', views.NewView.as_view(), name='new_view'),

]
