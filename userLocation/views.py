from django.core.mail.backends import console
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point, point
from . import models
from django.shortcuts import render
from django.apps import apps

from .models import Profile
from .models import GolfCourse


# Create your views here.
def update_location(request):
    try:
        user_profile = models.Profile.objects.get(user=request.user)
        if not user_profile:
            raise ValueError("Can't get User details")
        golfcoursename = request.POST.get("Course", False)
        lat = request.POST["Latitude"]
        lon = request.POST["Longitude"]

        location = request.POST["location"].split(",")
        lon_lat = [float(part) for part in location]
        lon, lat = lon_lat
        map_coords_point = Point(lon_lat, srid=4326)

        user_profile.Latitude = lat
        user_profile.Longitude = lon
        user_profile.location = map_coords_point
        user_profile.Favourite_Course = golfcoursename
        user_profile.save()
        return JsonResponse({"message": f"Set location to lon{lon},lat:{lat}."}, status=200)
    except Exception as e:
        raise e
        # return JsonResponse({"message": JSON.stringify(e)},status=400)


@login_required()
def Add_GolfCourse(request):
    try:

        golfcourse = models.GolfCourse()
        coursename = request.POST.get("courseName", False)
        lat = request.POST["latitude"]
        lon = request.POST["longitude"]

        Courselocation = request.POST["location"].split(",")
        lon_lat = [float(part) for part in Courselocation]
        lon, lat = lon_lat
        golfcourse_coords_point = Point(lon_lat, srid=4326)

        golfcourse.latitude = lat
        golfcourse.longitude = lon
        golfcourse.location = golfcourse_coords_point
        golfcourse.golfCourseName = coursename
        golfcourse.save()
        return JsonResponse({"message": f"Golf Course has been added"}, status=200)
    except Exception as e:
        raise e
        # return JsonResponse({"message": JSON.stringify(e)},status=400)


@login_required()
def map_view(request):
    golfcourse = GolfCourse.objects.all()
    return render(request, "map.html", {"golfcourse": golfcourse})
