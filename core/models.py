from uuid import uuid4
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class BaseManager(models.Manager):

    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated at')
    objects = BaseManager()

    class Meta:
        abstract = True
