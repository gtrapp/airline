from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="flights_index"),
    path("<int:flight_id>", views.flight, name="fck_flight"),
    path("<int:flight_id>/book", views.book, name="fck_book"),
]