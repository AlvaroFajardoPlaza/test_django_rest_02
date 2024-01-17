from django.urls import path, include
from . import views

app_name = "crm"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("register", views.register, name="register"),
    path("my_login", views.my_login, name="my_login"),
    path("logout", views.logout, name="logout")
]
