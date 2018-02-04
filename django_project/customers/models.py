# Third Party
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('countries.Country', on_delete=models.PROTECT, related_name='+')

    def __str__(self):
        return self.name
