from django.db import models
from foodpool.v1.core.models import TimestampedModel, CanadaAddressModel, AvailabilityModel


class MenuManager(models.Manager):
    def create(self, **required_fields):

        menu = self.model(**required_fields)
        menu.save()

        return menu


class MenuGroups(TimestampedModel):
    name = models.TextField()


class MenuItems(AvailabilityModel, TimestampedModel):
    objects = MenuManager()

    dishName = models.TextField()
    description = models.TextField()
    group = models.ForeignKey(MenuGroups, on_delete=models.PROTECT)
    calories = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)


class MenuOptions(TimestampedModel):
    menu = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    minOptions = models.IntegerField()
    maxOptions = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.CheckConstraint(check=models.Q(minOptions__lte=models.F("maxOptions")),
                                   name="optionConstraint")
        ]


class MenuOptionChoices(TimestampedModel):
    menuOptions = models.ForeignKey(MenuOptions, on_delete=models.CASCADE)
    choice = models.TextField()
    price = models.IntegerField()
    calories = models.IntegerField()
    minChoices = models.IntegerField()
    maxChoices = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.CheckConstraint(check=models.Q(minChoices__lte=models.F("maxChoices")),
                                   name="choiceConstraint")
        ]


class Restaurant(TimestampedModel):
    name = models.TextField()
    description = models.TextField()
    menu = models.ForeignKey(MenuItems, on_delete=models.PROTECT)


class RestaurantLocation(AvailabilityModel, CanadaAddressModel, TimestampedModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    isOpen = models.BooleanField(default=False)


