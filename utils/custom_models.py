import uuid
from django.db import models


class CustomBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True  # This ensures Django does not create a separate table for CustomBaseModel


