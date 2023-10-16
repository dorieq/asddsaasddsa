from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    file = models.FileField(upload_to='media/')
    title = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.id}: {self.title}'