from django.shortcuts import render

def index(request):
  return render(request, "core/index.html")

def book_a_flight(request):
  return render(request, "core/book_a_flight.html")

def plan_a_trip(request):
  return render(request, "core/plan_a_trip.html")

def community(request):
  return render(request, "core/community.html")