from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):

    """ Reservation Status Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.reservations.count()
