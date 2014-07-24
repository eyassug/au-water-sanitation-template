from django.db import models
from django.utils.encoding import smart_unicode

countrycode = models.ForeignKey('CountryCode')
name = models.CharField(max_length=100, null=False, blanck=True)
Latitude = models.DecimalField(max_digits=19, decimal_places=10, null=False)
longitude = models.DecimalField(max_digits=19, decimal_places=10, null=False)
isActive = models.BooleanField()

