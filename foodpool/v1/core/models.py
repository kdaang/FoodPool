from django.core.validators import RegexValidator
from django.db import models


###
# TIMES
###
class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']


class Calendar():
    WEEKDAYS = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday")
    ]


class AvailabilityModel(models.Model):
    weekday = models.IntegerField(choices=Calendar.WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        abstract = True
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)


###
# ADDRESSES
###


class CanadaAddress:
    NL = 'NL'
    PE = 'PE'
    NS = 'NS'
    NB = 'NB'
    QC = 'QC'
    ON = 'ON'
    MB = 'MB'
    SK = 'SK'
    AB = 'AB'
    BC = 'BC'
    YT = 'YT'
    NT = 'NT'
    NU = 'NU'

    provinces = [
        (NL, 'Newfoundland and Labrador'),
        (PE, 'Prince Edward Island'),
        (NB, 'Nova Scotia'),
        (NS, 'New Brunswick'),
        (QC, 'Quebec'),
        (ON, 'Ontario'),
        (MB, 'Manitoba'),
        (SK, 'Saskatchewan'),
        (AB, 'Alberta'),
        (BC, 'British Columbia'),
        (YT, 'Yukon'),
        (NT, 'Northwest Territories'),
        (NU, 'Nunavut')
    ]

    CAN = 'CAN'
    countries = [
        (CAN, 'Canada')
    ]


class CanadaAddressModel(models.Model):
    address_1 = models.CharField(max_length=254)
    address_2 = models.CharField(max_length=254)

    city = models.CharField(max_length=254)
    province = models.CharField(max_length=254, choices=CanadaAddress.provinces)
    postal_code = models.CharField(max_length=6, validators=[RegexValidator(regex=r'[A-Za-z]\d[A-Za-z]\d[A-Za-z]\d')])
    country = models.CharField(max_length=6, default=CanadaAddress.CAN,
                               choices=CanadaAddress.countries)

    class Meta:
        abstract = True

    REQUIRED_FIELDS = ['address_1', 'city', 'province', 'postal_code']
