from django.db import models

# Create your models here.


class bengaliPoems(models.Model):
    title = models.CharField(name='title', max_length=500)
    poet = models.CharField(name='poet', max_length=500)
    poem = models.CharField(name='poem', max_length=50000)
