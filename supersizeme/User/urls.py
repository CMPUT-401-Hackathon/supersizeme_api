from django.urls import path

from . import views

urlpatterns = [
    # ex: /User/test/
    path('<str:userName>/UpdateUser/', views.updateUser, name='updateUser'),
]