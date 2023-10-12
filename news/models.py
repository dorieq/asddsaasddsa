from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    text = models.TextField()
    file = models.FileField(upload_to='media/')

class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

