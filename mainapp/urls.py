from django.urls import path
from .views import main_index

app_name = "mainapp"

urlpatterns=[
    path("", main_index, name="main-index"),
]
