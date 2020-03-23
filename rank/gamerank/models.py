from django.db import models

# Create your models here.


class uprank(models.Model):
    uname = models.CharField(max_length=250)
    rank = models.CharField(max_length=250)

