from django.db import models

# Create your models here.


class Info(models.Model):
    access_token = models.CharField(max_length=200)
    client_id = models.CharField(max_length=200)
    client_secret = models.CharField(max_length=200)
    store_hash = models.CharField(max_length=200)


