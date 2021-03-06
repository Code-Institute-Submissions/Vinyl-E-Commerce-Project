from django.db import models
from productsVinyls.models import Vinyl
# Create your models here.


# Model for the vinyls order checkout form
class vinyl_Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


# Model for the Order Line Vinyl in the checkout
class OrderLineVinyl(models.Model):
    order = models.ForeignKey(vinyl_Order, null=False)
    vinyl = models.ForeignKey(Vinyl, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.vinyl.artist, self.vinyl.price)