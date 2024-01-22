from django.db import models
from core.models import BaseModel
from users.models import User


class Chat(BaseModel):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )


class Message(BaseModel):
    content = models.CharField(
        max_length=4096,
        null=True, blank=True
    )
    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    ...
