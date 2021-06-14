from django.conf.urls import url
from django.urls.resolvers import URLPattern 
from common import views

urlpatterns=[
    url(r'^department/$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),


]