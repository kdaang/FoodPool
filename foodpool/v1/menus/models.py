from django.db import models
from foodpool.v1.core.models import TimestampedModel, CanadaAddressModel, AvailabilityModel


class MenuManager(models.Manager):
    def create(self, **required_fields):

        menu = self.model(**required_fields)
        menu.save()

        return menu


class MenuGroup(TimestampedModel):
    name = models.TextField()


class Menu(AvailabilityModel, TimestampedModel):
    objects = MenuManager()

    dishName = models.TextField()
    description = models.TextField()
    group = models.ForeignKey(MenuGroup, on_delete=models.PROTECT)
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class MenuOptions(TimestampedModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    minOptions = models.IntegerField()
    maxOptions = models.IntegerField()

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.CheckConstraint(check=models.Q(minOptions__lte=models.F("maxOptions")),
                                   name="optionConstraint")
        ]


class MenuOptionChoices(TimestampedModel):
    menuOptions = models.ForeignKey(MenuOptions, on_delete=models.CASCADE)
    choice = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.IntegerField()
    minOptions = models.IntegerField()
    maxOptions = models.IntegerField()

    class Meta(TimestampedModel.Meta):
        constraints = [
            models.CheckConstraint(check=models.Q(minOptions__lte=models.F("maxOptions")),
                                   name="optionConstraint")
        ]


class Restaurant(TimestampedModel):
    name = models.TextField()
    description = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)


class RestaurantLocation(AvailabilityModel, CanadaAddressModel, TimestampedModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


