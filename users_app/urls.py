from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('create_user', views.create),
    path('success_page', views.success),
    path("delete_user", views.delete),
]