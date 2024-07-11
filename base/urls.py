from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/",views.room_list,name="room_list"),
    path("roomcreation/",views.create_room,name="create_room"),
    path("login/",views.loginPage, name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("register/",views.registerPage,name="register")
]