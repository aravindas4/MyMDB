import uuid
from django.db import models
from model_utils.models import TimeStampedModel


class Base(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    created_by = models.CharField(max_length=250, null=True, blank=True)
    modified_by = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        abstract = True

    def created_date(self):
        return self.created.strftime("%d %b %Y").upper()

    def created_date_time(self):
        return self.created.strftime("%d-%m-%Y %H:%M:%S")

    def modified_date(self):
        return self.modified.strftime("%d %b %Y").upper()

    def modified_date_time(self):
        return self.modified.strftime("%d-%m-%Y %H:%M:%S")
