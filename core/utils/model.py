from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at']

    created_at = models.DateTimeField(auto_now_add=True, help_text='time which this object was created')
    modified_at = models.DateTimeField(auto_now=True, help_text='time which this object was modified')