import re
import requests
import json
from . import serializers, models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required(login_url='/users/signin')
def plan_a_trip_view(request):
  return render(request, "plannedtrips/plan_a_trip.html")

def planned_trip_view(request, id):
  planned_trip = models.PlannedTrip.objects.get(id=id)
  return render(request, "plannedtrips/planned_trip.html", {"planned_trip": planned_trip})

@api_view(["POST"])
def plan_trip(request):
  if request.method == "POST":
    serializer = serializers.PlanATripSerializer(data=request.data)
    if serializer.is_valid():
      prompt = serializer.validated_data["prompt"]
      print(prompt)
      headers = {
        "Authorization": f"Bearer {settings.AUTH_TOKEN}",
        "Content-Type": "application/json"
      }
      body = {
        'model': 'gpt-3.5-turbo',
                'messages': [
                    {'role': 'system', 'content': 'You are an AI travel planner. Structure your response with each day starting on a new line prefixed by "Day: ", followed by key-value pairs for Activity, Location, Accommodation, Sightseeing Options, and Cost, separated by a colon and a space (e.g., "Activity: Local Exploration"). Use budget as part of your planning.'},
                   {'role': 'user', 'content': prompt}
                ]
      }
      url = settings.AI_URL

      response = requests.post(url=url, headers=headers, json=body)
      if response.status_code == 200:
        response_data = response.json()
        gpt_response = handle_plan_trip(response_data)
        planned_trip = models.PlannedTrip.objects.create(gpt_response=gpt_response)
        planned_trip.save()
        return Response({"planned_trip_id": planned_trip.id})
      else:
        return Response({"error": "An error occurred"})
      

def handle_plan_trip(json_data):
    data = json_data['choices'][0]['message']['content']
    lines = re.split(r'\n+', data)
    itinerary_details = []
    current_day = {}

    for line in lines:
        line = line.strip()
        if line.startswith('Day'):
            if current_day:
                itinerary_details.append(current_day)
            current_day = {'Day': line.split(':', 1)[1].strip()}
        elif ':' in line:
            key, value = line.split(':', 1)
            current_day[key.strip()] = value.strip()

    if current_day:
        itinerary_details.append(current_day)

    return itinerary_details

