from django.urls import path
from .views import main_index, new_doc

app_name = "mainapp"

urlpatterns=[
    path("", main_index, name="main-index"),
    path("new_doc/", new_doc, name="new-doc"),
]
