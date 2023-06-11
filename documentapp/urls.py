from django.urls import path
from . import views


app_name = "documentapp"

urlpatterns=[
    path("document/<int:id>", views.show_document, name="show-document"),
]
