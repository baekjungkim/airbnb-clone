from django.contrib import admin
from . import models


@admin.register(models.Reservation, models.Status)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    pass
