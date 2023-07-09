from django.urls import path
from . import views


app_name = "documentapp"

urlpatterns=[
    path("document/<int:id>", views.show_document, name="show-document"),
    path("document/<int:id>/delete", views.delete_document, name="delete-document"),
    path("document/<int:id>/edit", views.edit_document, name="edit-document"),


]
