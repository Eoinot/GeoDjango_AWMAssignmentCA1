import csv
from userLocation.models import GolfCourse
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = "loads data from DublinGolfCourses.csv"

    def handle(self, *args, **options):
        # GolfCourse.objects.all().delete()
        csv_file = "DublinGolfCourses.csv"

        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                latitude = float(row["Latitude"])
                longitude = float(row["Longitude"])
                golfCourseName = row["Golf_Course_Name"]
                map_coords_point = Point((longitude, latitude), srid=4326)

                golfcourse = GolfCourse(
                    latitude=latitude,
                    longitude=longitude,
                    golfCourseName=golfCourseName,
                    location=map_coords_point
                )
                golfcourse.save()

        print("The csv file has been successfully imported")
