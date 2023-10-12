from django.db import models
from django.utils.translation import gettext_lazy as _

class Banner(models.Model):
    image_desktop = models.ImageField()
    image_mobile = models.ImageField()
    link = models.URLField(_("Link"), max_length=200)
    title = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.id}: {self.title}'