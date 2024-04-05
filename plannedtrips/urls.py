from django.urls import path
from . import views

urlpatterns = [
    path("plan-a-trip", views.plan_a_trip_view, name="plan_a_trip"),
    path("planned-trip/<str:id>", views.planned_trip_view, name="planned_trip"),
    path("plan-trip", views.plan_trip, name="plan_a_trip_api")
]
