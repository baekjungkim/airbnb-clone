from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    s_country = request.GET.get("country", "KR")
    s_room_type = int(request.GET.get("room_type", 0))
    price = request.GET.get("price", 0)
    guests = request.GET.get("guests", 0)
    bedrooms = request.GET.get("bedrooms", 0)
    beds = request.GET.get("beds", 0)
    baths = request.GET.get("baths", 0)
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    s_house_rules = request.GET.getlist("house_rules")

    form = {
        "city": city,
        "s_country": s_country,
        "s_room_type": s_room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "s_house_rules": s_house_rules,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    house_rules = models.HouseRule.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
        "house_rules": house_rules,
    }

    filter_args = {}

    if city != "":
        filter_args["city__startswith"] = city

    filter_args["country__exact"] = s_country

    if s_room_type != 0:
        filter_args["room_type__pk"] = s_room_type

    if int(price) != 0:
        filter_args["price__lte"] = price

    if int(guests) != 0:
        filter_args["guests__gte"] = guests

    if int(bedrooms) != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if int(beds) != 0:
        filter_args["beds__gte"] = beds

    if int(baths) != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book__exact"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)
    # s_amenities = request.GET.getlist("amenities")
    # s_facilities = request.GET.getlist("facilities")
    # s_house_rules = request.GET.getlist("house_rules")

    print(filter_args)

    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms},)
