from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Converstation Model Definition """

    participnts = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    converstation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} : {self.text}"
