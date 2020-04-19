from django.db import models
from foodpool.v1.core.models import CanadaAddressModel, TimestampedModel


class Address(CanadaAddressModel, TimestampedModel):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name="addresses")