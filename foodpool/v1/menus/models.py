from django.db import models
from foodpool.v1.core.models import TimestampedModel, CanadaAddressModel, AvailabilityModel


class MenuManager(models.Manager):
    def create(self, **required_fields):

        menu = self.model(**required_fields)
        menu.save()

        return menu


class Menu(TimestampedModel):
    skip_id = models.CharField(max_length=36, unique=True)


class MenuGroups(TimestampedModel):
    name = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)


class MenuGroupAvailability(AvailabilityModel, TimestampedModel):
    group = models.ForeignKey(MenuGroups, on_delete=models.PROTECT)


class MenuItems(TimestampedModel):
    objects = MenuManager()

    name = models.TextField()
    description = models.TextField()
    group = models.ForeignKey(MenuGroups, on_delete=models.PROTECT)
    calories = models.IntegerField(null=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)


class MenuOptions(TimestampedModel):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.CheckConstraint(check=models.Q(minimum__lte=models.F("maximum")),
                                   name="optionConstraint")
        ]


class MenuOptionChoices(TimestampedModel):
    menu_option = models.ForeignKey(MenuOptions, on_delete=models.CASCADE)
    choice = models.TextField()
    price = models.IntegerField()
    calories = models.IntegerField(null=True)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.CheckConstraint(check=models.Q(minimum__lte=models.F("maximum")),
                                   name="choiceConstraint")
        ]


class Restaurant(TimestampedModel):
    name = models.TextField()
    shortName = models.TextField()
    description = models.TextField(null=True)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)


class RestaurantLocation(CanadaAddressModel, TimestampedModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)


class RestaurantLocationAvailability(AvailabilityModel):
    restaurant_location = models.ForeignKey(RestaurantLocation, on_delete=models.PROTECT)


