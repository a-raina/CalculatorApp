from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.calculator_list, name='calculator_list'),
]