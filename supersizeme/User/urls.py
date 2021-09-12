from django.urls import path

from . import views

urlpatterns = [
    # ex: /User/test/
    path('<str:username>/UpdateUser/', views.updateUser, name='updateUser'),
    # ex: /User/TestUser/userLogin/
    path('<str:username>/userLogin/', views.userLogin, name='userLogin'),
    # ex: /User/TestUser/GetUserDetails/
    path('<str:username>/GetUserDetails/', views.getUserDetails, name='getUserdetails')
]