from django.db import models

from foodpool.v1.core.models import TimestampedModel
from foodpool.v1.menus.models import RestaurantLocation, MenuItems, MenuOptionChoices


class Order(TimestampedModel):
    total_price = models.IntegerField()
    special_instructions = models.TextField()
    restaurant_location = models.ForeignKey(RestaurantLocation, on_delete=models.PROTECT)


class OrderItems(TimestampedModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_item = models.ForeignKey(MenuItems, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class OrderOptionChoices(TimestampedModel):
    order_item = models.ForeignKey(OrderItems, on_delete=models.PROTECT)
    menu_option_choice = models.ForeignKey(MenuOptionChoices, on_delete=models.CASCADE)
    quantity = models.IntegerField()
