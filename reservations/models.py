from django.db import models
from core import models as core_models
from rooms import models as room_models


class Status(room_models.AbstractItem):
    """ Status Model Definition """

    class Meta:
        verbose_name_plural = "Status"


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    status = models.ManyToManyField("Status", blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"
