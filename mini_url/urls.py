from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten, name='shorten'), # url(r'^shorten$', views.shorten, name='shorten'),
    path('', views.list_all, name='list_all'), # url(r'^$', views.list_all, name='list_all'),
    path('redirect/<str:code>', views.redirect, name='redirect'), # url(r'^(?P<code>\w{6}/$', views.redirect, name='redirect'),
]