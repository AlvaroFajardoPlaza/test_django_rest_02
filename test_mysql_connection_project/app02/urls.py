from django.urls import path
from . import views

app_name = "app02"
urlpatterns = [
    path("api/", views.get_all_data, name="get_all_data"),
    path("post/", views.post_new_character, name="post_new_character"),
]