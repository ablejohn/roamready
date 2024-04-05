from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book-a-flight", views.book_a_flight, name="book_a_flight"),
    path("plan-a-trip", views.plan_a_trip, name="plan_a_trip"),
    path("community", views.community, name="community")
]
