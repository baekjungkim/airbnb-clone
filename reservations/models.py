from django.db import models
from django.utils import timezone
from core import models as core_models
from rooms import models as room_models


class Status(room_models.AbstractItem):
    """ Status Model Definition """

    class Meta:
        verbose_name_plural = "Reservation Status"


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    status = models.ForeignKey(
        "Status", related_name="reservations", blank=True, on_delete=models.PROTECT
    )
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

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
