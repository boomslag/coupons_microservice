from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
import uuid

class Coupon(models.Model):
    types = (
        ('courses', 'Courses'),
        ('products', 'Products'),
        ('games', 'Games'),
        ('music', 'Music'),
        ('videos', 'Videos'),
        ('movies', 'Movies'),
        ('assets', 'Assets'),
        ('art', 'Art'),
        ('software', 'Software'),
        ('licenseKeys', 'License Keys'),
        ('documents', 'Documents'),
        ('datasets', 'Datasets'),
        ('templates', 'Templates'),
    )
    
    id =                models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    user = models.UUIDField(blank=True, null=True)
    fixed_price_coupon = models.ForeignKey('FixedPriceCoupon', on_delete=models.CASCADE, blank=True, null=True)
    percentage_coupon = models.ForeignKey('PercentageCoupon', on_delete=models.CASCADE, blank=True, null=True)
    content_type = models.CharField(choices=types, max_length=20, default='courses')
    object_id = models.UUIDField(blank=True, null=True)

    def __str__(self):
        return self.name

class FixedPriceCoupon(models.Model):
    id =                models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    uses = models.IntegerField()


class PercentageCoupon(models.Model):
    id =                models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    discount_percentage = models.IntegerField()
    uses = models.IntegerField()
