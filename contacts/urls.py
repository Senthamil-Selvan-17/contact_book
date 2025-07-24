from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("new_contact", views.new_contact, name="new_contact"),
    path("show_contact", views.show_contact, name="show_contact")
]