from django.urls import path

from . import views
from calrecs import views as calviews

urlpatterns = [
    # ex: /User/test/
    path('<str:userName>/UpdateUser/', views.updateUser, name='updateUser'),
    path('<str:username>/calrecs/', calviews.calrecs),
]