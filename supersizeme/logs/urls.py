from django.urls import path

from . import views

urlpatterns = [
    # ex: /log/username/2021-09-11/
    path('<str:username>/<str:date>/', views.log, name='log'),
    path('<str:username>/', views.logs),
]