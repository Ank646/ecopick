from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("dise", views.gh, name="dise"),
    # path("listofpickers", views.doc, name="doc"),
    path("register", views.register, name="register"),
    path("verify/<str:token>", views.verify, name="verify"),
    # path("check", views.po, name="po"),
    # path("center", views.center, name="center"),
    path("shop", views.shop, name="shop"),
    path("registeruser", views.registeruser, name="registeruser"),
    path("greencenter", views.greencenter, name="greencenter"),
    path("logout", views.logout, name="logout"),
    path("login", views.login, name="login"),
    path("book", views.book, name="book"),
    path("order", views.orderr, name="order"),
    path("myorders", views.myorders, name="myorders"),

]
