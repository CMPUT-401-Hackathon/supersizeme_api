from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<str:name>/', views.item_info),
    path('category/<str:category>/', views.category_info),
    path('delete/<str:name>/', views.delete),
    path('add/<str:name>/', views.add),
]