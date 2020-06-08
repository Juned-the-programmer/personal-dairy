from django.db import models

# Create your models here.
class diary(models.Model):
    date_create = models.DateField(auto_now_add=True)
    desc = models.TextField(max_length=100000000000)
    name = models.CharField(max_length=100)

    