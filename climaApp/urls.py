from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('page-error', views.page_error, name='page-error'),
    
]