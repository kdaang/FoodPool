from django.db import models
from django.template.defaultfilters import upper
from foodpool.v1.core.models import CanadaAddressModel, TimestampedModel


class AddressManager(models.Manager):
    def create(self, **required_fields):
        required_fields['postal_code'] = upper(required_fields['postal_code'])

        address = self.model(**required_fields)
        address.save()

        return address


class Address(CanadaAddressModel, TimestampedModel):
    objects = AddressManager()

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name="addresses")