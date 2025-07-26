from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("new_contact", views.new_contact, name="new_contact"),
    path("show_contact", views.show_contact, name="show_contact"),
    path("edit_contact", views.edit_contact, name="edit_contact"),
    path("delete_contact", views.delete_contact, name="delete_contact")
]