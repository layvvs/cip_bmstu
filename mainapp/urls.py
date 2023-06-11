from django.urls import path
from . import views


app_name = "mainapp"

urlpatterns=[
    path("", views.main_index, name="main-index"),
    path("new_doc/", views.new_doc, name="new-doc"),
    path("document/<int:id>", views.show_document, name="show-document"),
]
